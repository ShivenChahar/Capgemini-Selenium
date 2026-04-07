import requests
import urllib3

urllib3.disable_warnings()
base = "https://www.shoppersstack.com/shopping"

token = ""
UserID = ""

def register_user():
    body = {
    "city": "Jaipur",
    "country": "India",
    "email": "johnwick101@gmail.com",
    "firstName": "John",
    "gender": "MALE",
    "lastName": "Wick",
    "password": "12345678",
    "phone": 9898941111,
    "state": "Rajasthan",
    "zoneId": "ALPHA"
    }

    response = requests.post(f"{base}/shoppers",json=body,verify=False)

    print(response.status_code)
    print(response.text)

def user_login():
    global token, UserID
    body = {
        "email": "johnwick101@gmail.com",
        "password": "12345678",
        "role": "SHOPPER"
    }
    response = requests.post(f"{base}/users/login",json=body,verify=False)
    print(response.status_code)
    print(response.json())
    token = response.json()["data"]["jwtToken"]
    UserID = response.json()["data"]["userId"]
    print(f"TokenValue:{token}")
    print(f"UserID:{UserID}")

def get_user_info():
    header = {"Authorization": f"Bearer {token}"}
    response = requests.get(f"{base}/shoppers/{UserID}",headers = header,verify=False)
    print(response.status_code)
    print(response.json())

register_user()
user_login()
get_user_info()
