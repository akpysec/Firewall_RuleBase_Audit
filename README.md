<p align="center">
  <img src="https://user-images.githubusercontent.com/48283299/135756072-3291c51c-7f2a-4cda-86ee-561c5d42561b.png"/>
</p>

#

## Description

Rule Base Audit was designed by security me AKPySec aka Andrey Kolihanov. It is meant to provide a security-oriented view of the IPv4 Rule Bases from various type firewalls (Tufin, FortiGate, Palo-Alto, Checkpoint & More). Once consultant exported IPV4 policy in .csv or .txt format, all auditing checks may be performed offline.

Contact me via <akpysec@gmail.com>.

### Types of Checks Supported

Currently the following checks are supported:

- Broad assignment with object "Any" within Source / Destination / Service fields
- Disabled rules
- No Log rules
- Crossed rules (Two-way rules)
- Worst rules (rules with multiple findings)

## Installation & Setup
Rule Base Audit is written in Python and supports the following versions:
* Python 3.8
* Python 3.9

Download & Install Python https://www.python.org/downloads/

It is always a best practice to run programs in virtualenv, so don't forget to run:
* pip install virtualenv

### Via Git
Make sure you have Git installed https://git-scm.com/downloads

    $ git clone https://github.com/akpysec/Firewall_RuleBase_Audit
    $ cd Firewall_RuleBase_Audit
    $ virtualenv -p python3 venv
    $ source venv/bin/activate
    $ pip install -r requirements.txt
    $ python RuleBaseAudit.py --help

## Usage

Rule Base Audit is run through the CLI:

    $ python3 RuleBaseAudit.py --path /path/to/folder/with/file-s --file-extension txt --fw-vendor fortigate
    $ python3 RuleBaseAudit.py --path /path/to/folder/with/file-s --file-extension csv --fw-vendor tufin

#### Add HERE GIF - later

Once this has completed, it will generate an .xlsx report including findings:

#### Add HERE GIF - later

The above report was generated by running Rule Base Audit against dummy files from https://github.com/akpysec/Firewall_RuleBase_Audit/tree/master/tests.


