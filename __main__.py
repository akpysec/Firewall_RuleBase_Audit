# Local Project Imports
from policy_providers import fortigate, tufin
from engine.check_engine import any_srv, any_dst, any_src, disabled, track_logs, worst_rules, crossed_rules, creating_excel_sheet
from engine.cli_flags import args
from engine.bar_chart import stats_chart


checks = [
    any_srv, any_dst, any_src, disabled, track_logs, worst_rules, crossed_rules
]

AUDIT_OUTPUT = 'Audit-Checks.xlsx'
creating_excel_sheet(
    output_name=AUDIT_OUTPUT,
    fw_type=args.policy_provider,
    policy_file_path=args.path)

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
            file_name=AUDIT_OUTPUT,
            sheet_name=check.__name__.upper().replace('_', ' ')
        )

    elif args.policy_provider.lower() == 'tufin':
        tufi = check(
            dataframe=tufin.files_reader_and_parser(
                path_to_files=args.path,
                file_extension=args.file_extension,
                encoding_files=args.encoding
            ),
            file_name=AUDIT_OUTPUT,
            sheet_name=check.__name__.upper().replace('_', ' ')
        )


print("-" * 23)
print(f"DONE!!!")
print("-" * 23)
