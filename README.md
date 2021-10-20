<p align="center">
  <img src="https://user-images.githubusercontent.com/48283299/135764873-62804f9f-a58d-45ec-a1b2-0c33b04c31f1.png"/>
</p>

#

## Description

I designed Rule Base Audit to provide a security-oriented view of the IPv4 Rule Base from different vendors and 
Firewall types (Tufin, FortiGate, Palo-Alto, Checkpoint & More). 
Once consultant exported IPV4 policy in .csv or .txt format, all auditing checks may be performed offline.

### Types of Checks Supported

Currently the following checks are supported:

- Broad assignment with object "Any" within Source / Destination / Service fields
- Disabled rules
- No Log rules
- Crossed rules (Two-way rules)
- Worst rules (rules with multiple findings)

#### Caveats
.CSV exported files sometimes are exported as "broken", you may get an error:

    "pandas.errors.ParserError: Error tokenizing data. C error: Expected 2 fields in line x, saw y Occurs"

- To fix this issue just open the file and make a "save as" copy of it, 
you can even overwrite original file.

## Installation & Setup
Rule Base Audit is written in Python and supports the following versions:
* Python 3.8
* Python 3.9

Download & Install [Python](https://www.python.org/downloads/)

It is always a best practice to run programs in virtualenv, so don't forget to run:
* pip install virtualenv

The required libraries can be found in the 
[requirements.txt](https://github.com/akpysec/Firewall_RuleBase_Audit/blob/master/requirements.txt) file.
### Via Git
Make sure you have [Git](https://git-scm.com/downloads) installed 

    git clone https://github.com/akpysec/Firewall_RuleBase_Audit
    cd Firewall_RuleBase_Audit
    virtualenv -p python3 venv
    source venv/bin/activate
    pip install -r requirements.txt
    python Firewall_RuleBase_Audit --help

## Usage
You can view acceptable formats in 
[./tests](https://github.com/akpysec/Firewall_RuleBase_Audit/tree/master/tests) folder, 
if yours differs I would like to know!

Rule Base Audit is run through the CLI:

    $ python3 Firewall_RuleBase_Audit --path /path/to/folder/with/file/s --file-extension txt --policy-provider fortigate
    OR
    $ python3 Firewall_RuleBase_Audit -P /path/to/folder/with/file/s -F csv -PP tufin

#### Add HERE GIF - later

Once this has completed, it will generate an .xlsx report including findings:

#### Add HERE GIF - later

The above report was generated by running Rule Base Audit against dummy files 
from [./tests](https://github.com/akpysec/Firewall_RuleBase_Audit/tree/master/tests) folder dummy files.

## License
Firewall RuleBase Audit is released under the
[GNU Public License](https://github.com/akpysec/Firewall_RuleBase_Audit/LICENSE)

## Contact
Contact me via <akpysec@gmail.com>.

[comment]: <> ([^1]: )