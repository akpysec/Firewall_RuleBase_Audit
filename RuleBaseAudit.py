from policy_providers import fortigate, tufin
from engine.check_engine import any_srv, any_dst, any_src, disabled, track_logs, worst_rules
from engine.cli_flags import args
from engine.bar_chart import stats_chart

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
            print(f'{check.__name__} \tFINDING')
            forti.to_csv(f"{args.path}\\{check.__name__}.csv")
        elif forti is None:
            print(f"{check.__name__} \tPASS")
        else:
            print("Something else happened")
    elif args.policy_provider == 'tufin':
        tufi = check(
            dataframe=tufin.files_reader_and_parser(
                path_to_files=args.path,
                file_extension=args.file_extension,
                encoding_files=args.encoding
            )
        )
        if tufi is not None:
            print(f'{check.__name__} \tFINDING')
            tufi.to_csv(f"{args.path}\\{check.__name__}.csv")
        elif tufi is None:
            print(f"{check.__name__} \tPASS")
        else:
            print("Something else happened")

# # For later
# if args.bar_chart:
#     stats_chart(finding_type="str", times_found=int)

