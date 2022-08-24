# vManage API

## Description

Script to demonstrate the Cisco SD-WAN Controller (vManage) API usage

It includes a class and functions to handle authentication process and to send basic API requests to vManage

It also has the option to upload sofware images files to vmanage, files need to be saved under the images folder

This repository is going to be used for training and there are some test files that are only relevant for it, if you are using the app on your own please ignore them

## Installation

Clone repository and use pip to install requirements

    pip install -r requirements.txt

## Configuration

There are 2 configuration files under config folder

    .
    ├─ config/
        └─ config.yaml
        └─ payload.json

YAML file is pre-configured to connect to Cisco DEVNET SD-WAN 20.4 Always On Sandbox

JSON file is pre-configured with the data for a test user to vmanage

Edit files to connect to a different vmanage or provide a different payload as needed

## Execution

Use CLI help to display the execution options

    python vmanage_api.py --help

There are no mandatory parameters, if none provided then it will be assumed to be a GET request, NO payload, TABLE printing and the '/device/monitor' resource

Please mind that most of the POST, PUT or DELETE requests will require the use of the --payload argument, body to upload needs to be saved on the config/payload.json file, a sample user is saved there now as an example

Pre-build print options are only available for GET requests, other methods will only display a success or fail message


Execution examples

    python vmanage_api.py -r "/template/policy/list/tloc"

or

    python vmanage_api.py -r "/device/ip/ipRoutes?deviceId=10.10.1.11"

or

    python vmanage_api.py -a POST -p -r "/admin/user"

or 

    python vmanage_api.py -u

or sample mode (NO ARGUMENTS)

    python vmanage_api.py

## References

    https://developer.cisco.com/docs/sdwan/

    https://devnetsandbox.cisco.com/RM/Diagram/Index/a4ab71bc-f7a0-4d63-bedb-05a051818569?diagramType=Topology


## Author

Raul Gomez

    raul.agobe@gmail.com

    rgomezbe@cisco.com


## Comments

Special thanks to my friend Luis Vargas for the help testing