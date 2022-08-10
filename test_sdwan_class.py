# Import the class module
from modules.sdwan_manager import sdwan_manager

# Provide the basic connection attributes statically
vmanage = 'sandbox-sdwan-2.cisco.com'
port = '443'
username = 'devnetuser'
password = 'RG!_Yw919_83'

# Start a session to vmanage (new class instance)
session = sdwan_manager(vmanage,port,username,password)

# Test printing the cookie and token
print('Cookie:' , session.cookie)
print('Token:' , session.token)

# Define an action ,resource ('/device/monitor') and an empty body
action = 'GET'
resource = '/device/monitor'
body = {}

# Send an api request
response = session.send_request(action,resource,body)

# Print the response
print('Response Object:' , response)
print('Response Text:' , response.text)
print('Response DATA: ', response.json()['data'])
print('Response Status Code:' , response.status_code)
print('Response Method: ',response.request.method)