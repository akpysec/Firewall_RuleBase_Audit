<p align="center">
  <img src="https://user-images.githubusercontent.com/48283299/135756072-3291c51c-7f2a-4cda-86ee-561c5d42561b.png"/>
</p>

#

## Description

Rule Base Audit was designed by security me AKPySec aka Andrey Kolihanov. It is meant to provide a security-oriented view of the IPv4 Rule Bases from various type firewalls (Tufin, FortiGate, Palo-Alto, Checkpoint & More). Once consultant exported IPV4 policy in .csv or .txt format, all auditing checks may be performed offline.

The project team can be contacted at <scoutsuite@nccgroup.com>.

### Types of Checks Supported

Currently the following checks are supported:

- Broad assignment with object "Any" within Source / Destination / Service fields
- Disabled rules
- No Log rules
- Crossed rules (Two-way rules)
- Worst rules (rules with multiple findings)

## Installation
### Via Git

    $ git clone https://github.com/akpysec/Firewall_RuleBase_Audit
    $ cd Firewall_RuleBase_Audit
    $ virtualenv -p python3 venv
    $ source venv/bin/activate
    $ pip install -r requirements.txt
    $ python RuleBaseAudit.py --help


## Usage

Rule Base Audit is run through the CLI:

    // For FortiGate IPv4 Policy
    python3 RuleBaseAudit.py --path /path/to/folder/with/file-s --file-extension txt --fw-vendor fortigate
    // For Tufin exported csv files
    python3 RuleBaseAudit.py --path /path/to/folder/with/file-s --file-extension csv --fw-vendor tufin

[comment]: <> (![Running Rule Base Audit]&#40;https://user-images.githubusercontent.com/להשלים.gif&#41;)

Once this has completed, it will generate an .xlsx report including findings:

[comment]: <> (![Rule Base Audit Report]&#40;https://user-images.githubusercontent.com/להשלים.gif&#41;)

The above report was generated by running Rule Base Audit against dummy files from https://github.com/akpysec/Firewall_RuleBase_Audit/tree/master/tests.


