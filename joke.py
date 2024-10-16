# импортируем библиотеку requests для выполнения HTTP-запросов
import requests

# берём URL по которому хотим получать запросы
url = "https://api.chucknorris.io."
print(url)

# выполняем GET-запрос к указанному URL и сохраняем ответ в переменной result
result = requests.get(url)
print("Status Code: "  + str(result.status_code))

# проверяем статус код запроса, ожидаем 200 (успех) и выводим результаты в консоль
assert 200 == result.status_code

# если статус код равен 200, выводим сообщение об успешности, иначе выводим сообщение об ошибке.
if result.status_code == 200:
    print("Успешно, статус код верен!")
else:
    print("Ошибка, статус код не верен!")

# выводим текст ответа из переменной result в формате JSON
print(result.json)
4