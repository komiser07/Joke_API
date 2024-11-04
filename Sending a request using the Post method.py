import requests


class test_new_location():

    def test_add_place(self):
        base_url = "https://rahulshettyacademy.com"
        post_resource = "/maps/api/place/add/json"
        get_resource = "/maps/api/place/get/json"
        place_id_file = "place_id.txt"

        key = "?key=qaclick123"
        json_location = {
            "location": {
                "lat": -38.383494,
                "lng": 33.427362
            }, "accuracy": 50,
            "name": "Frontline house",
            "phone_number":
                "(+91) 983 893 3937",
            "address": "29, side layout, cohen 09",
            "types": [
                "shoe park",
                "shop"
            ],
            "website": "http://google.com",
            "language": "French-IN"
        }
        post_url = base_url + post_resource + key
        print(post_url)
        result_post = requests.post(post_url, json=json_location)
        print(result_post.json())

        check_response_post = result_post.json()

        place_id = check_response_post.get('place_id')
        with open(place_id_file, 'w') as f:
            for _ in range(5):
                f.write(f"{place_id}\n")

        get_url = f"{base_url}{get_resource}{key}&place_id={place_id}"
        print(get_url)


start = test_new_location()
start.test_add_place()
