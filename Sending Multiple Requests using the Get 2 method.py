import requests


class TestCreateJokeCategory():

    def __init__(self, base_url):
        self.categories = None
        self.base_url = base_url
    # вывод списка категорий
    def list_of_all_categories(self):
        url = f"{self.base_url}/categories"
        result = requests.get(url)
        self.categories = result.json()
        print(self.categories)

    def test_joke_for_user_selected_category(self):
        # Шаг 1: Запрос категории от пользователя
        user_category = input("Выберите категорию для получения шутки: ")

        # шаг 2: проверка, что выбранная пользователем категория, есть в списке категорий
        assert user_category in self.categories, f"Категория '{user_category}' не найдена в списке категорий: {self.categories}"
        print("Данная категория есть в списке всех категорий\n")

        # шаг 2: Запрос одной шутки по категории, запрошенную пользователем
        response = requests.get(f"{self.base_url}/random", params={"category": user_category})
        data = response.json()
        joke = data['value']
        print(joke)


start = TestCreateJokeCategory('https://api.chucknorris.io/jokes')
start.list_of_all_categories()
start.test_joke_for_user_selected_category()
