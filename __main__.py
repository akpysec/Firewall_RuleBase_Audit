# Local Project Imports
from policy_providers import fortigate, tufin
from engine.check_engine import any_srv, any_dst, any_src, disabled, track_logs, worst_rules, crossed_rules
from engine.cli_flags import args
from engine.bar_chart import stats_chart

# Libraries Import
import pandas as pd
import openpyxl
import datetime

checks = [
    any_srv, any_dst, any_src, disabled, track_logs, worst_rules, crossed_rules
]

# Couldn't find a way to remove the first sheet('Sheet1'), so I added some lame info
AUDIT_OUTPUT = 'Audit-Checks.xlsx'
writer = pd.ExcelWriter(AUDIT_OUTPUT, engine='xlsxwriter')
base_info = {
    'Date': [datetime.datetime.today()],
    'Firewall Type': [args.policy_provider.upper()],
    'Policy Path': [args.path]
}
base_frame = pd.DataFrame(base_info)
base_frame.to_excel(writer, sheet_name="Flags", index=False)
writer.close()

print("-" * 23)
print("Performing checks:")
print("-" * 23)

for check in checks:
    if args.policy_provider.lower() == 'fortigate':
        forti = check(
            dataframe=fortigate.create_df(
                rule_base_as_nested_dict=fortigate.rule_base_parsing(
                    raw_dataframe=fortigate.files_reader(
                        path_to_files=args.path,
                        file_extension=args.file_extension,
                        encoding_files=args.encoding
                    )
                )
            ),
            file_name=AUDIT_OUTPUT
            # sheet=check.__name__.upper().replace('_', ' ')
        )

    elif args.policy_provider.lower() == 'tufin':
        tufi = check(
            dataframe=tufin.files_reader_and_parser(
                path_to_files=args.path,
                file_extension=args.file_extension,
                encoding_files=args.encoding
            )
        )


print("-" * 23)
print(f"DONE!!!")
print("-" * 23)
