# SAMPLE DATA
sample_data = [{'device-model': 'vmanage', 'device-type': 'vmanage', 'system-ip': '10.10.1.1', 'host-name': 'vmanage', 'site-id': '101', 'layoutLevel': 1, 'status': 'normal'}, {'device-model': 'vsmart', 'device-type': 'vsmart', 'system-ip': '10.10.1.5', 'host-name': 'vsmart', 'site-id': '101', 'layoutLevel': 2, 'status': 'normal'}, {'device-model': 'vedge-cloud', 'device-type': 'vbond', 'system-ip': '10.10.1.3', 'host-name': 'vbond', 'site-id': '101', 'layoutLevel': 3, 'status': 'normal'}, {'device-model': 'vedge-CSR-1000v', 'device-type': 'vedge', 'system-ip': '10.10.1.11', 'host-name': 'dc-cedge01', 'site-id': '101', 'layoutLevel': 4, 'status': 'normal'}, {'device-model': 'vedge-CSR-1000v', 'device-type': 'vedge', 'system-ip': '10.10.1.13', 'host-name': 'site1-cedge01', 'site-id': '1001', 'layoutLevel': 4, 'status': 'normal'}, {'device-model': 'vedge-CSR-1000v', 'device-type': 'vedge', 'system-ip': '10.10.1.15', 'host-name': 'site2-cedge01', 'site-id': '1002', 'layoutLevel': 4, 'status': 'normal'}, {'device-model': 'vedge-cloud', 'device-type': 'vedge', 'system-ip': '10.10.1.17', 'host-name': 'site3-vedge01', 'site-id': '1003', 'layoutLevel': 4, 'status': 'normal'}]

# Import the support module
from modules.support_manager import load_yaml_config,get_arguments,print_tabulate,print_formatted_data,load_payload

# Use terminal to provide different arguments and print them
arguments = get_arguments()
print(arguments)

# Load and print the values from a YAML file
variables = load_yaml_config('config/config.yaml')
print(variables)
print(variables['VMANAGE'])
print(variables['USERNAME'])

# Load and print the values from a JSON file
body = load_payload('config/payload.json')
print(body)

# Use print_formatted function to print a dictionary
print_formatted_data(sample_data)

# Use print_tabulate function to print a table from a dictionary
print_tabulate(sample_data)
