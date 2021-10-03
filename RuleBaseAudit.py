import sys
from fw_parsers import fortigate, tufin

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


