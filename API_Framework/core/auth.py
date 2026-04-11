from API.login_API import LoginAPI
from utils.read_data import read_json

loginAPI = LoginAPI()

def get_auth_data():
    data = read_json("test_data/login.json")
    payload = data["valid_user"]

    response = loginAPI.login(payload)

    print("STATUS:", response.status_code)
    print("RESPONSE:", response.json())

    assert response.status_code == 200

    res_json = response.json()

    token = res_json["data"]["jwtToken"]
    shopper_id = res_json["data"]["userId"]

    return {
        "token": token,
        "shopper_id": shopper_id
    }