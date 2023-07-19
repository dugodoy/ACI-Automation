# ACI-NDO-Automation

Ansible files used to apply configuration on Cisco ACI APIC and NDO (Nexus Dashboard Orchestrator), here are some comments about the files listed in this repository:
 
- aci_hosts.yml – Used as the ansible inventory file, which we list the apics and mso information (root folder)
- playbooks/playbook_initial_config.yml - Used to apply configuration to bring up ACI Fabric tasks listed below:
  - Apply Best Practices
  - Register Nodes
  - Configure Rack Objects
  - Associate Nodes to Rack
  - Configure Out-of-Band IP Address
  - Configure BGP ASN and Associate to the Fabric
  - Configure Spines as Route Reflectors
  - Configure Fabric Switch Policy Groups
  - Configure Fabric Spine Profiles
  - Configure Fabric Leaf Profiles
  - Configure DNS Servers
  - Configure DNS Domain
  - Configure Syslog  
  - Configure SNMP  
  - Configure Timezone  
  - Configure NTP  
  - Configure Tacacs  
- playbooks/playbook_access_pol.yml – Used to configure access policies objects listed below:
  - Configure Interface Policies
  - Configure Leaf Switch Profile
  - Configure Leaf Switch Selector and Associate to Switch Profile
  - Configure VPC Domain
  - Configure Domains
  - Configure VLAN Encap
  - Associate Domain to VLAN Pool
  - Configure Interface Policy Group Type PC
  - Configure Interface Policy Group Type VPC
  - Configure Interface Policy Group Type Access
  - Configure Leaf Interface Profiles, Interface Selectors and Associate Policy Groups
  - Associate Leaf Interface Profile to Switch Profile
- playbooks/playbook_mso_objects.yml – Used to created Bridge Domain, EPG and associate physical domain to EPG on Nexus Dashboard Orchestrator.
- playbooks/playbook_mso-static_ports.yml – Used to create static ports on EPGs on Nexus Dashboard Orchestrator.
- templates/leaf_int_pro.xml.j2 – Jinja template used to generate APIC XML to create Interface profiles, interface selectors and associate policy groups to interface selectors.
- templates/vlan_encap.xml.j2 – Jinja template used to generate APIC XML to create VLAN Pool and VLAN Blocks.
- aci_config/config-apic01.xlsx – Spreadsheet used to generate APIC configuration.
- aci_config/config-mso.xlsx – Spreadsheet used to generate NDO configuration.
- aci_config/excel_to_csv.py – Script used to generate CSVs from excel spreadsheet, apic01 or apic02 must be informed because inside the playbook it uses the inventory host name to apply the configuration to the correct apic in case both apic01 and apic02 should be configured at the same time.  
`python excel_to_csv.py config-apic01.xlsx apic01`  
`python excel_to_csv.py config-mso.xlsx`
 
**To run a playbook from the root folder:**  
`ansible-playbook -i aci_hosts.yml playbooks/playbook_access_pol.yml`
 
**Playbook tags were included on each playbook, to check the ones available use the following command:**  
`ansible-playbook -i aci_hosts.yml playbooks/playbook_access_pol.yml –list-tags`
 
**To check Tasks available on the playbooks, use the following command:**  
`ansible-playbook -i aci_hosts.yml playbooks/playbook_access_pol.yml –list-tasks`
 
**Installing python and creating virtual environment:**
| Procedure | Description | Command |
| --- | --- | --- |
| install python 3.8 at least | download from python.org |
| install python virtual environment | | pip3 install virtualenv |
| create virtual environment | | python3.8 -m venv folder_name |
| activate virtual environment | | source /folder_name/bin/activate |

**Additional packages required to run the ansible playbooks and script excel_to_csv.py:**
| Package | Description | Command |
| --- | --- | --- |
| install ansible | Install ansible Core package | pip3 install ansible |
| read_csv | Ansible module used to read CSV file content, it is available through collection community.general | ansible-galaxy collection install community.general |
| cisco.aci | Ansible modules to manage ACI objects | ansible-galaxy collection install cisco.aci |
| cisco.mso | Ansible modules to manage Cisco ACI MSO objects | ansible-galaxy collection install cisco.mso |
| cisco.nd | Ansible module to allow MSO configuration hosted on Nexus Dashboard applicance | ansible-galaxy collection install cisco.nd |
| install jmespath | Python package used to query data on a JSON format | pip3 install jmespath |
| install xmljson | Python package used by aci.rest ansible module | pip3 install xmljson |
| install pandas | Python package used by convert excel spreadsheet to csv file | pip3 install pandas |
| install openpyxl | Python package used by convert excel spreadsheet to csv file | pip3 install openpyxl |
| install lxml | Python package used to manipulate XML files | pip3 install lxml |
