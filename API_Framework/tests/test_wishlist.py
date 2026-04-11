from API.wishlist_API import WishlistAPI
from utils.read_data import read_json

def test_add_to_wishlist(auth_data, headers):
    wishlist_api = WishlistAPI()
    data = read_json("test_data/wishlist.json")

    # res_json = response.json()
    # shopper_id = res_json["data"]["userId"]
    shopper_id = auth_data["shopper_id"]

    response = wishlist_api.add_to_wishlist(
        shopper_id= shopper_id,
        headers = headers,
        product_id = data["productId"],
        quantity = data["quantity"]
    )

    assert response.status_code in [200, 201, 409], f"Failed:{response.text}"

def test_get_wishlist(auth_data, headers):
    wishlist_api = WishlistAPI()
    shopper_id = auth_data["shopper_id"]
    response = wishlist_api.get_wishlist(shopper_id, headers = headers)
    print(response.json())

    assert response.status_code == 200