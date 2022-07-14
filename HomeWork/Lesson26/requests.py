import json
import requests

# Получение списка авторов
response = requests.get(url='https://fakerestapi.azurewebsites.net/api/v1/Authors').json()
print(json.dumps(response, indent=3))

# Получение конкретного автора по его id
response1 = requests.get(url='https://fakerestapi.azurewebsites.net/api/v1/Authors/3').json()
print(json.dumps(response1, indent=3))
print()

# Добавить новую книгу
body = dict(id=0, title="string", description="string", pageCount=0, excerpt="string",
            publishDate="2022-07-13T20:38:05.537Z")
response2 = requests.post(url='https://fakerestapi.azurewebsites.net/api/v1/Books', json=body).json()
print(response2)
print()

# Добавить нового пользователя
user = {'id': 1, 'userName': 'Yaroslav', 'password': '123'}
response3 = requests.post(url='https://fakerestapi.azurewebsites.net/api/v1/Users', json=user).json()
print(response3)
print()

# Обновить данные для книги под номером 10
data = dict(id=10, title="Qwerty", description="Qwerty", pageCount=1, excerpt="Qwerty",
            publishDate="2022-07-13T20:38:05.537Z")
response4 = requests.put(url='https://fakerestapi.azurewebsites.net/api/v1/Books/10', json=data)
print(response4.status_code)
print(response4.json())
print()

# Удалить пользователя под номером 4
response5 = requests.delete(url='https://fakerestapi.azurewebsites.net/api/v1/Users/4')
print(response5.status_code)
