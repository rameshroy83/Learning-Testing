# Importing required libraries used

import requests
import urllib3

# Creating a session

session = requests.session()

# Excluding exception related to self signed certificate
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Setting IP address and credentials

ip_addr = "10.97.169.5"
cred = {"username": "admin", "password": "HTS!ndi@"}

# Initiating a Post Request to start the login session

login = session.post(f"https://{ip_addr}/rest/v10.10/login", data=cred, verify=False)
print(login.status_code)
#print(login.cookies)
#logout = session.post(f"https://{ip_addr}/rest/v10.10/logout")
#print(logout.status_code)