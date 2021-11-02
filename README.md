<p align="center">
  <img src="https://user-images.githubusercontent.com/48283299/135764873-62804f9f-a58d-45ec-a1b2-0c33b04c31f1.png"/>
</p>

#

## Description

I designed Rule Base Audit to provide a security-oriented view of the IPv4 Rule Base from different vendors and 
Firewall types (Tufin, FortiGate - Tested) future Development will support Palo-Alto, Checkpoint & More). 
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

It is always a best practice to run programs in virtualenv, so don't forget to install:
* pip install virtualenv

The required libraries can be found in the 
[requirements.txt](https://github.com/akpysec/Firewall_RuleBase_Audit/blob/master/requirements.txt) file.

[comment]: <> (### Via PIP &#40;UNDER CONSTRUCTION - NOT YET AT PYPI&#41;)
    
[comment]: <> (    python -m venv Firewall_RuleBase_Audit/venv)

[comment]: <> (    source Firewall_RuleBase_Audit/venv/Scripts/activate)

[comment]: <> (    pip install Firewall_RuleBase_Audit)

[comment]: <> (    Firewall_RuleBase_Audit --help)

### Via Git (Bash)
Make sure you have [Git](https://git-scm.com/downloads) installed 

    git clone https://github.com/akpysec/Firewall_RuleBase_Audit
    python -m venv Firewall_RuleBase_Audit/venv
    source Firewall_RuleBase_Audit/venv/Scripts/activate
    pip install -r Firewall_RuleBase_Audit/requirements.txt
    python Firewall_RuleBase_Audit --help

![Installation](https://user-images.githubusercontent.com/48283299/139966956-d66968b4-37f9-405f-b9e9-7735ae572d6c.gif)

## Usage
You can view acceptable formats in 
[./tests](https://github.com/akpysec/Firewall_RuleBase_Audit/tree/master/tests) folder.

Rule Base Audit is run through the CLI:

    python Firewall_RuleBase_Audit --path {path} --file-extension {txt/csv} --policy-provider {provider}

Tufin run:
![tufin_run](https://user-images.githubusercontent.com/48283299/139966962-397cb001-97c9-4480-9478-32466514b758.gif)

Forti run:
![forti_run](https://user-images.githubusercontent.com/48283299/139966971-75856343-ecb2-4a65-b0e6-182750383462.gif)

Once this has completed, it will generate an .xlsx report including findings.

The above report was generated by running Rule Base Audit against dummy files 
from [./tests](https://github.com/akpysec/Firewall_RuleBase_Audit/tree/master/tests) folder dummy files.

## License
Firewall RuleBase Audit is released under the
[GNU Public License](https://github.com/akpysec/Firewall_RuleBase_Audit/LICENSE)

## Contact
Contact me via <akpysec@gmail.com>.

[comment]: <> ([^1]: )
