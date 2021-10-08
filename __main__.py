from policy_providers import fortigate, tufin
from engine.check_engine import any_srv, any_dst, any_src, disabled, track_logs, worst_rules
from engine.cli_flags import args
from engine.bar_chart import stats_chart
import colored
from colored import fg, bg, attr, stylize


BOLD_RED = colored.fg("red") + colored.attr("bold")
BOLD_GREEN = colored.fg("green") + colored.attr("bold")
BOLD_ORANGE = colored.fg("dark_orange_3a") + colored.attr("bold")

checks = [
    any_srv, any_dst, any_src, disabled, track_logs, worst_rules
]

for check in checks:

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
            print(stylize(f'{check.__name__} \tFINDING', BOLD_RED))
            forti.to_csv(f"{args.path}\\{check.__name__}.csv")
        elif forti is None:
            print(stylize(f"{check.__name__} \tPASS", BOLD_GREEN))
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
            print(stylize(f'{check.__name__} \tFINDING', BOLD_RED))
            tufi.to_csv(f"{args.path}\\{check.__name__}.csv")
        elif tufi is None:
            print(stylize(f"{check.__name__} \tPASS", BOLD_GREEN))
        else:
            print(stylize("Something else happened", BOLD_ORANGE))

# # For later
# if args.bar_chart:
#     stats_chart(finding_type="str", times_found=int)

