from policy_providers import fortigate, tufin
from engine.check_engine import any_srv, any_dst, any_src, disabled, track, worst
from engine.cli_flags import args

if args.rule_base_provider == 'fortigate':
    any_src(
        dataframe=fortigate.create_df(
            rule_base_as_nested_dict=fortigate.rule_base_parsing(
                raw_dataframe=fortigate.files_reader(
                    path_to_files=args.path,
                    file_extension=args.file_extension,
                    encoding_files=args.encoding
                )
            )
        )
    ).to_csv(f"{args.path}\\any_source.csv")

elif args.rule_base_provider == 'tufin':
    any_src(
        dataframe=tufin.files_reader_and_parser(
            path_to_files=args.path,
            file_extension=args.file_extension,
            encoding_files=args.encoding
        )
    ).to_csv(f"{args.path}\\any_source.csv")

