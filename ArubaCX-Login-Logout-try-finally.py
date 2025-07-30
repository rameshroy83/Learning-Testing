import urllib3
import requests

session = requests.session()

ip_addr = "10.97.169.5"
cred = {"username": "admin", "password": "1234"}
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

try:
    login = session.post(f"https://{ip_addr}/rest/v10.10/login", data=cred, verify=False)
    print(login.status_code)
    print(login.cookies)

finally:
    logout = session.post(f"https://{ip_addr}/rest/v10.10/logout", data=cred, verify=False)
    print(logout.status_code)