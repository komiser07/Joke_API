import requests

class TestCreateJokeCategory():

    url = "https://api.chucknorris.io/jokes/random"

    def test_create_random_joke_positive(self, category, expected_status_code):
        path_random_joke_category = f'?category={category}'
        url_random_joke_category = self.url + path_random_joke_category
        print(url_random_joke_category)

        result = requests.get(url_random_joke_category)
        print(result.json())

        print(f'Статус-код: {result.status_code}')
        assert result.status_code == expected_status_code
        print("Статус-код корректен")

        check_joke = result.json()
        joke_value = check_joke.get('value')
        print(joke_value)

        joke_category = check_joke.get('categories')
        print(joke_category)
        assert joke_category[0] == category
        print('Категория корректна')

        print('Тест прошел успешно')

    def test_create_random_joke_negative(self, category, expected_status_code):
        path_random_joke_category = f'?category={category}'
        url_random_joke_category = self.url + path_random_joke_category
        print(url_random_joke_category)

        result = requests.get(url_random_joke_category)
        print(result.json())

        print(f'Статус-код: {result.status_code}')
        assert result.status_code == expected_status_code
        print("Статус-код корректен")

        check_joke = result.json()
        print(check_joke)

        error = check_joke.get('error')
        print(error)
        assert error == "Not Found"
        print('Полу Error корректно')


start = TestCreateJokeCategory()
# start.test_create_random_joke_positive('animal', 200)
start.test_create_random_joke_negative('anim', 404)
start.test_create_random_joke_negative('', 404)
start.test_create_random_joke_negative('spot', 404)
print("Тест прошел успешно")