import requests

# response = requests.get("https://petstore.swagger.io/v2/pet/findByStatus?status=sold")
# response = requests.get("https://petstore.swagger.io/v2/store/inventory")
#
#
# # Using the response variable
# print(response.status_code)
# print(response.text)
# print(response.json())
# dict = (response.json())
# print(dict["Not Available"])
# expected = 200
# actual = response.status_code
# assert actual == expected, "Wrong response"


def post():
    payload = {
        "id": 101,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggy",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    }

    response = requests.post("https://petstore.swagger.io/v2/pet", json=payload)
    print(response.status_code)
    print(response.json())

def get():
    response1 = requests.get("https://petstore.swagger.io/v2/pet/101")
    print(response1.status_code)
    print(response1.json())

def delete():
    response2 = requests.delete("https://petstore.swagger.io/v2/pet/101")
    print(response2.status_code)
    print(response2.json())

post()
get()
delete()