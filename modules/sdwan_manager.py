import requests
from urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)
from time import time
import os

class sdwan_manager():


    def __init__(self,server,port,username,password):

        self.username = username
        self.password = password
        self.server = server
        self.port = port
        self.host = server + ':' + port
        self.cookie = self.get_auth_cookie()
        self.token = self.get_auth_token()

    
    def get_auth_cookie(self):

        url = f"https://{self.host}/j_security_check"

        payload = f'j_username={self.username}&j_password={self.password}'
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}

        response = requests.request("POST", url, headers=headers, data=payload, verify=False)

        cookie = response.cookies.get_dict()['JSESSIONID']

        return cookie


    def get_auth_token(self):

        url = f"https://{self.server}/dataservice/client/token"

        payload={}
        headers = {
        'Cookie': f'JSESSIONID={self.cookie}'
        }

        response = requests.request("GET", url, headers=headers, data=payload, verify=False)

        token = response.text

        return token


    def send_request(self,action,resource,body):

        url = f'https://{self.host}/dataservice{resource}'

        headers = {
        'X-XSRF-TOKEN': self.token,
        'Cookie': f'JSESSIONID={self.cookie}',
        'Content-Type': 'application/json',
        }

        response = requests.request(action, url, headers=headers, data=body, verify=False)

        return response
                

    def logout(self):

        url = f"https://{self.host}/logout?nocache={str(int(time()))}"

        payload={}

        headers = {
        'Cookie': f'JSESSIONID={self.cookie}',
        }

        response = requests.request("GET", url, headers=headers, data=payload, verify=False)

        message = 'Session closed!' if response.status_code == 200 else 'Problems closing session'
        print(message)


    def upload_image(self,image):

        upload_url = f"https://{self.host}/dataservice/device/action/software/package"

        headers = {
        'X-XSRF-TOKEN': self.token,
        'Cookie': f'JSESSIONID={self.cookie}',
        }

        try:

            upload_file = {'name': open(f"images/{image}", "rb")}
            size = int(os.stat(f"./images/{image}").st_size / 1024)
            print(f"Uploading {image} - {size} KB")

            response = requests.request("POST", url=upload_url, headers=headers, files=upload_file, verify=False)

            if response.status_code == 200:
                print(f"{image} upload finished")


            else:
                print("Status code received: ", response.status_code)
                print(response.text)     

        
        except FileNotFoundError:

                print("File Not Found")

        except Exception as e:

                print("Problems during upload process")
                print(e)