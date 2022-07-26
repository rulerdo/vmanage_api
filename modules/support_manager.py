from argparse import ArgumentParser
import yaml
from tabulate import tabulate
import json

def get_arguments():

    parser = ArgumentParser(description='Arguments for custom requests')
    parser.add_argument('--resource', '-r', default=None, help='full resource for custom request ex. python sdwan_vmanage_api.py -r "/device/control/connections" ')
    parser.add_argument('--action', '-a', choices=['GET','POST','PUT','DELETE'], default='GET', help='HTTP method to use with the requests')
    parser.add_argument('--payload', '-p', action="store_true", help='use to include the paylod file under config/payload.json')
    parser.add_argument('--tab','-t', action="store_true", help='use to print a table format')
    arguments = parser.parse_args()

    return arguments


def load_yaml_config(config_file):

    with open(config_file, 'r') as f:
        variables = yaml.safe_load(f)

    for key in variables.keys():
        if not variables[key]:
            variables[key] = input(f'{key}: ')

    return variables


def load_payload(payload_file):

    body = {}

    try:
        if payload_file:
            with open(payload_file) as f:
                body = json.dumps(json.load(f))
    
    except Exception:

        print(f'Problems loading file {payload_file}')

    return body


def print_formatted_data(data):

    for element in data:

        for k,v in element.items():
            print(f'{k} : {v}')
        
        print('')


def print_tabulate(data):

    headers = data[0].keys()
    table = [element.values() for element in data]    

    print(tabulate(table,headers=headers,tablefmt="pretty"),'\n')
