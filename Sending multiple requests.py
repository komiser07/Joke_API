import requests


class TestCreateJokeCategory():

    def __init__(self, base_url):
        # Инициализация словаря для хранения шуток по категориям
        self.jokes = {}
        self.base_url = base_url

    # Получение списка всех категорий
    def list_of_all_categories(self):
        url = f"{self.base_url}/categories"
        result = requests.get(url)
        self.categories = result.json()
        print(self.categories)

    # Получение одной шутки по каждой категории
    def get_one_joke_per_category(self):
        for category in self.categories:
            url = f"{self.base_url}/random?category={category}"
            response = requests.get(url)
            data = response.json()
            joke = data['value']
            if category not in self.jokes:
                self.jokes[category] = []
            self.jokes[category].append(joke)
            print(f"Категория: {category}\nшутка: {joke}")

start = TestCreateJokeCategory('https://api.chucknorris.io/jokes')
start.list_of_all_categories()
start.get_one_joke_per_category()
