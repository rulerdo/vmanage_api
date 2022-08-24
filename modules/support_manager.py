from argparse import ArgumentParser
import yaml
from tabulate import tabulate
import json
import sys
import os

def get_arguments():

    parser = ArgumentParser(description='Arguments for custom requests')
    parser.add_argument('--resource', '-r', default=None, help='full resource for custom request ex. python sdwan_vmanage_api.py -r "/device/control/connections" ')
    parser.add_argument('--action', '-a', choices=['GET','POST','PUT','DELETE'], default='GET', help='HTTP method to use with the requests')
    parser.add_argument('--payload', '-p', action="store_true", help='use to include the paylod file under config/payload.json')
    parser.add_argument('--tab','-t', action="store_true", help='use to print a table format')
    parser.add_argument('--upload', '-u', action="store_true", help='use to upload a software file from images folder to vmanage')
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


def parse_request_response(response):

    data = {}
    failure = False
    action = response.request.method

    if action == 'GET':

        try:
            data = response.json()['data']

        except Exception as error:

            print('ERROR:',error)
            failure = True

    elif response.status_code in range (200,300):

        if response.status_code == 200:
            print(f'{action} request completed successfully')

    if failure or response.status_code not in range (200,300):
        print(f'Problems with {action} request')
        print('URL:',response.url)
        print('TEXT:',response.text)
        print('STATUS CODE:',response.status_code)
        sys.exit(1)

    return data
    

def print_formatted_data(data):

    for element in data:

        for k,v in element.items():
            print(f'{k} : {v}')
        
        print('')


def print_tabulate(data):

    headers = data[0].keys()
    table = [element.values() for element in data]    

    print(tabulate(table,headers=headers,tablefmt="pretty"),'\n')


def get_image_from_folder():

    dir_list = os.listdir('./images')
    acceptable_extensions = ('bin', 'tar', 'gz')
    file_list = [file for file in dir_list if file.endswith(acceptable_extensions)]
    i = 1

    print('Files available on image folder:')
    for file in file_list:
        print(f'{i}.- {file}')
        i += 1

    while True:

        user_input = input('Type the file number to upload: ')

        try:
            option = int(user_input) - 1
            image = file_list[option]
            break
        
        except ValueError:
            print('Invalid option:')
            print('Please try again, use the file number')

        except IndexError:
            print('Invalid option:')
            print('Please try again, selected number out of range')
        
        except Exception as e:
            print('Invalid option:')
            print(e)
            print('Please try again')

    return image