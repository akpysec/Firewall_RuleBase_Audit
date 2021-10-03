from fw_parsers import fortigate, tufin
from engine.check_engine import any_srv, any_dst, any_src, disabled, track, worst
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-P', '--path',
                    required=True,
                    default=None,
                    dest='path',
                    help='Provide a Path to a folder with exported IPv4 policy file/s',
                    type=str
                    )

parser.add_argument('-F', '--file-extension',
                    required=True,
                    default=None,
                    dest='file_extension',
                    help='Provide a file/s extension type',
                    type=str
                    )

parser.add_argument('-R', '--rule-base-provider',
                    required=True,
                    default=None,
                    dest='rule_base_provider',
                    help='Provide a Firewall rule base provider name (Tufin, Checkpoint, Palo-Alto, FortiGate)',
                    type=str
                    )

parser.add_argument('-E', '--encoding',
                    default='windows-1256',
                    dest='encoding',
                    help='Provide a file/s encoding',
                    type=str
                    )

args = parser.parse_args()

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
    ).to_csv("C:\\Users\\andreyk\\PycharmProjects\\RuleBaseAudit\\any_source.csv")

elif args.rule_base_provider == 'tufin':
    any_src(
        dataframe=tufin.files_reader_and_parser(
            path_to_files=args.path,
            file_extension=args.file_extension,
            encoding_files=args.encoding
        )
    ).to_csv("C:\\Users\\andreyk\\PycharmProjects\\RuleBaseAudit\\any_source.csv")


