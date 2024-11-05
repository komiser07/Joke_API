import requests


class TestNewLocation():

    def __init__(self, base_url, key):
        self.base_url = base_url
        self.key = key
        self.post_resource = "/maps/api/place/add/json"
        self.get_resource = "/maps/api/place/get/json"
        self.place_id_file = "place_id.txt"

    @staticmethod
    def generate_json_location(index):
        """Создаёт уникальные данные для каждого запроса, чтобы обеспечить разные place_id"""
        return {
            "location": {
                "lat": -38.383494 + index * 0.01,
                "lng": 33.427362 + index * 0.01
            }, "accuracy": 50,
            "name": f"Frontline house {index + 1}",
            "phone_number":
                "(+91) 983 893 3937",
            "address": f"29, side layout, cohen 09, {index + 1}",
            "types": [
                "shoe park",
                "shop"
            ],
            "website": "http://google.com",
            "language": "French-IN"
        }

    def multiple_places_and_check_place_ids(self):
        print("== Добавляем 5 уникальных мест и записываем их place_id в файл ==")
        with open(self.place_id_file, "w") as file:
            for i in range(5):
                post_url = f"{self.base_url}{self.post_resource}{self.key}"
                print(post_url)

                # Генерируем уникальные данные для каждого запроса
                json_location = self.generate_json_location(i)

                # POST-запрос для добавления нового места
                result_post = requests.post(post_url, json=json_location)
                print(result_post.json())

                check_response_post = result_post.json()
                place_id = check_response_post.get("place_id", [])

                # Записываем каждый уникальный place_id в файл
                file.write(f"{place_id}\n")

        # Чтение place_id из файла
        print("\n== Проверка существования каждого place_id из файла ==")
        with open(self.place_id_file, "r") as file:
            for line in file:
                place_id_from_file = line.strip()
                print(place_id_from_file)

                # GET-запрос для проверки существования каждого place_id
                get_url = f"{self.base_url}{self.get_resource}{self.key}&place_id={place_id_from_file}"
                result_get = requests.get(get_url)
                print(result_get.json())

                # Проверка, что GET-запрос успешен и place_id существует
                assert result_get.status_code == 200
                print(f"Place_id {place_id_from_file} успешно проверен и найден\n")


start = TestNewLocation('https://rahulshettyacademy.com', '?key=qaclick123')
start.multiple_places_and_check_place_ids()
