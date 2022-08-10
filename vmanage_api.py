from modules.support_manager import load_yaml_config,get_arguments,print_tabulate,print_formatted_data,load_payload
from modules.sdwan_manager import sdwan_manager


__copyright__ = "Copyright (c) 2022 Raul Gomez"
__version__   = "1.0.0"
__author__    = "Raul Gomez"
__email__     = "rgomezbe@cisco.com"
__url__       = "https://wwwin-github.cisco.com/rgomezbe/vmanage_api"

'''
python vmanage_api.py -a GET -r '/admin/user'
python vmanage_api.py -a POST -r '/admin/user' -p
python vmanage_api.py -a PUT -r '/admin/user/testpost' -p
python vmanage_api.py -a DELETE -r '/admin/user/testpost'
'''

if __name__ == '__main__':

    variables = load_yaml_config('config/config.yaml')
    args = get_arguments()

    vmanage = variables['VMANAGE']
    port = str(variables['PORT'])
    username = variables['USERNAME']
    password = variables['PASSWORD']

    session = sdwan_manager(vmanage,port,username,password)

    resource = args.resource
    action = args.action
    table = args.tab
    body = {}

    if args.payload:
        body = load_payload('config/payload.json') 

    if not resource and not table:
        resource = '/device/monitor'
        table = True

    data = session.send_request(action,resource,body)

    if not bool(data):
        print('Request returned no data')

    else:
        print_tabulate(data) if table else print_formatted_data(data)
        
    session.logout()