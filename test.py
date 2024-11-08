import requests

class BaseTest:
    def test_get_categories(self):
        url = f"https://api.chucknorris.io/jokes/categories"
        response = requests.get(url)
        data = response.json()
        categories = data['categories']

class TestCreateJoke:
    def test_get_joke_by_category(self, category):
        joke = BaseTest().test_get_joke_by_category(category)
        print(f"Категория: {category}\nШутка: {joke}")

if __name__ == '__main__':
    tc = TestCreateJoke()
    category = input("Какая категория шутки вас интересует? ")
    if category == '':
        print("Необходимо указать категорию шутки.")
    else:
        joke = tc.test_get_joke_by_category(category)
        print(f"Категория: {category}\nШутка: {joke}")