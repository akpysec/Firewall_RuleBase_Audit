# Local Project Imports
from policy_providers import fortigate, tufin
from engine.check_engine import any_srv, any_dst, any_src, disabled, track_logs, worst_rules, crossed_rules
from engine.cli_flags import args
from engine.bar_chart import stats_chart

# Packages Import
import colored
from colored import fg, attr, stylize
import pandas as pd
import openpyxl
import datetime

BOLD_RED = colored.fg("red") + colored.attr("bold")
BOLD_GREEN = colored.fg("green") + colored.attr("bold")
BOLD_ORANGE = colored.fg("dark_orange_3a") + colored.attr("bold")

checks = [
    any_srv, any_dst, any_src, disabled, track_logs, worst_rules, crossed_rules
]

AUDIT_OUTPUT = 'Audit-Checks.xlsx'
# Couldn't find a way to remove the first sheet('Sheet1'), so I added some lame info
writer = pd.ExcelWriter(AUDIT_OUTPUT, engine='xlsxwriter')
base_info = {
    'Date': [datetime.datetime.today()],
    'Firewall Type': [args.policy_provider.upper()],
    'Policy Path': [args.path]
}
base_frame = pd.DataFrame(base_info)
base_frame.to_excel(writer, sheet_name="Base Info", index=False)
writer.close()

for check in checks:
    findings = list() # Put here what found and then write to excel each
    if args.policy_provider == 'fortigate':
        forti = check(
            dataframe=fortigate.create_df(
                rule_base_as_nested_dict=fortigate.rule_base_parsing(
                    raw_dataframe=fortigate.files_reader(
                        path_to_files=args.path,
                        file_extension=args.file_extension,
                        encoding_files=args.encoding
                    )
                )
            )
        )
        if forti is not None:
            with pd.ExcelWriter(AUDIT_OUTPUT, mode='a', engine='openpyxl') as writer:
                forti.to_excel(writer, sheet_name=check.__name__.upper().replace('_', ' '), index=False)
            print(stylize(f'{check.__name__.upper()} \tFINDING', BOLD_RED))
        elif forti is None:
            print(stylize(f"{check.__name__.upper()} \tPASS", BOLD_GREEN))
        else:
            print(stylize("Something else happened", BOLD_ORANGE))

    elif args.policy_provider == 'tufin':
        tufi = check(
            dataframe=tufin.files_reader_and_parser(
                path_to_files=args.path,
                file_extension=args.file_extension,
                encoding_files=args.encoding
            )
        )
        if tufi is not None:
            with pd.ExcelWriter(AUDIT_OUTPUT, mode='a', engine='openpyxl') as writer:
                tufi.to_excel(writer, sheet_name=check.__name__.upper().replace('_', ' '), index=False)
            print(stylize(f'{check.__name__.upper()} \tFINDING', BOLD_RED))
        elif tufi is None:
            print(stylize(f"{check.__name__.upper()} \tPASS", BOLD_GREEN))
        else:
            print(stylize("Something else happened", BOLD_ORANGE))



# # For later
# if args.bar_chart:
#     stats_chart(finding_type="str", times_found=int)

