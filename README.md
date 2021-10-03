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

## Usage

Rule Base Audit is run through the CLI:

![Running Rule Base Audit](https://user-images.githubusercontent.com/להשלים.gif)

Once this has completed, it will generate an .xlsx report including findings:

![Rule Base Audit Report](https://user-images.githubusercontent.com/להשלים.gif)

The above report was generated by running Rule Base Audit against dummy files from https://github.com/akpysec/RuleBaseAudit/tests.


