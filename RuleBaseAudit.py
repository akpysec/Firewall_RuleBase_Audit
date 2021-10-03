import sys
from fw_parsers import fortigate, tufin
from engine.check_engine import any_srv, any_dst, any_src, disabled, track, worst

arguments = sys.argv

checks_functions = [
    any_src,
    any_dst,
    any_srv,
    disabled,
    track,
    worst
]

must_have_args = [
    '--path',
    '--file-extension',
    '--fw-vendor'
]

optional_args = [
    '--help',
    '--encoding-files'
]

for args in must_have_args:
    if args not in arguments:
        print(f'Missing argument "{args}"')
    else:
        if arguments[6] == 'fortigate':
            for check in checks_functions:
                check(fortigate.files_reader(
                    path_to_files=arguments[2],
                    file_extension=arguments[4]
                )
                )
        if arguments[6] == 'tufin':
            for check in checks_functions:
                check(tufin.files_reader_and_parser(
                    path_to_files=arguments[2],
                    file_extension=arguments[4]
                )
                )
