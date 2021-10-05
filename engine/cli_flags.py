import argparse

parser = argparse.ArgumentParser()

# Creating flags
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

parser.add_argument('-R', '--policy-provider',
                    required=True,
                    default=None,
                    dest='policy_provider',
                    help='Provide a Firewall rule base provider name - tufin | checkpoint | palo-alto | fortigate',
                    type=str
                    )

parser.add_argument('-E', '--encoding',
                    default='windows-1256',
                    dest='encoding',
                    help='Provide a file/s encoding (default is "windows-1256")',
                    type=str
                    )

parser.add_argument('-C', '--chart',
                    action="store_true",
                    dest='bar_chart',
                    help='Display a Bar Chart with stats',
                    )

args = parser.parse_args()
