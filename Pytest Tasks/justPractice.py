# import requests
# import urllib3
# urllib3.disable_warnings()
#
# base = "https://www.shoppersstack.com/shopping"
# token = ""
# UserID = ""
#
# def register_user():
#     body = {
#         "city": "Jaipur",
#         "country": "India",
#         "email": "johnwick101@gmail.com",
#         "firstName": "John",
#         "gender": "MALE",
#         "lastName": "Wick",
#         "password": "12345678",
#         "phone": 9898941111,
#         "state": "Rajasthan",
#         "zoneId": "ALPHA"
#     }
#     response = requests.post(f"{base}/shoppers", json = base, )
#     print(response.text)
#     print(response.json())
#
# def login():
#     global token, UserID
#     body = {
#         "email": "johnwick101@gmail.com",
#         "password": "12345678",
#         "role": "SHOPPER"
#     }
#     response = requests.post("f{base}/users/login", json = body)
#     UserID = response.json()["data"]["userID"]
#     token = response.json()["data"]["jwtToken"]
#     print(response.text)
#     print(response.json())
#
# def getUser()
#