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

for m_args, o_args in zip(must_have_args, optional_args):
    if m_args not in arguments:
        print(f'Missing argument "{m_args}"')
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
    if o_args == optional_args[0]:
        print('Required arguments:\n')
        print(must_have_args[0], '\tchoose path to folder with exported IPv4 policies')
        print(must_have_args[1], '\tchoose right extension of a file "txt/csv"')
        print(must_have_args[2], '\tchoose firewall vendor')
        print('Optional arguments:\n')
        print(optional_args[0], '\thelp - present options')
        print(optional_args[1], '\tselect encoding for csv')