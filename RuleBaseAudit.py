import sys
from fw_parsers import fortigate, tufin
from engine import check_engine

print('*' * 12)
print('How to run:')
print('*' * 12)
print('.\\python RuleBaseAudit.py --path "Disk:\\Path\\to\\files\\folder" --file-extension "csv or txt" --fw-vendor "tufin or fortigate"')
print('-' * 88)

arguments = sys.argv

must_have_args = [
    '--path',
    '--file-extension',
    '--fw-vendor'
]

for args in must_have_args:
    if args not in arguments:
        print(f'Missing argument "{args}"')
    else:
        if arguments[6] == 'fortigate':
            print(fortigate.files_reader(
                path_to_files=arguments[2],
                file_extension=arguments[4]
                )
            )
        if arguments[6] == 'tufin':
            print(tufin.files_reader_and_parser(
                path_to_files=arguments[2],
                file_extension=arguments[4]
                )
            )


