import requests


class TesCreatJoke:

    def test_create_random_joke(self, category: str):
        url = f"https://api.chucknorris.io/jokes/random?category={category}"
        print(url)

        # выполняем GET-запрос к указанному URL и сохраняем ответ в переменной result
        result = requests.get(url)
        print(result.json())
        print(f"Статус код: {result.status_code}")

        # Проверка: статус-код ответа должен быть 200
        assert result.status_code == 200
        print("Успешно, статус код верен!")

        # Проверка: шутка должна содержать категорию "animal"
        check_joke = result.json()
        assert category in check_joke['categories'], f"Ошибка: шутка не относится к категории {category}"
        print("Категория шутки совпадает с ожидаемой!")

        # Проверка: шутка должна содержать имя "Chuck"
        joke_text = check_joke['value']
        assert 'Chuck' in joke_text, "Ошибка: шутка не содержит имя 'Chuck'"
        print("Имя 'Chuck' в шутке найдено")

        print(joke_text)
        print("Тест прошёл успешно")


start = TesCreatJoke()
start.test_create_random_joke('sport')
    # "animal", "career", "celebrity", "dev", "explicit", "fashion", "food", "history"
    # "money", "movie", "music", "political", "religion", "science", "sport", "travel"
