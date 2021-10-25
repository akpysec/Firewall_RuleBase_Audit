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

parser.add_argument('-PP', '--policy-provider',
                    required=True,
                    default=None,
                    dest='policy_provider',
                    help=f'Provide a Firewall rule base provider name - Checkpoint | Fortigate | Tufin',
                    type=str
                    )

parser.add_argument('-E', '--encoding',
                    default='windows-1256',
                    dest='encoding',
                    help='Provide a file/s encoding (default is "windows-1256")',
                    type=str
                    )

args = parser.parse_args()
