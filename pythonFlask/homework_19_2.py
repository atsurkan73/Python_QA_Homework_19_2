import json
import requests
import os

# 1. зробить через POST upload якогось зображення на сервер

url_base = 'http://127.0.0.1:8080'
url = 'http://127.0.0.1:8080/upload?files=blanc.bmp'
file_name = 'blanc.bmp'

with open(f'ToSend/{file_name}', 'rb') as img:
  name_img= os.path.basename(f'ToSend/{file_name}')
  files= {'image': (f'{file_name}', img, 'MIME: image/*')}
  with requests.Session() as s:
    r = s.post(url,files=files)

# Перевірка статус-коду
if r.status_code == 201:
    created_data = r.json()  # отримання даних у форматі JSON
    print('Створено дані:', created_data)
else:
    print('Post request. Помилка. Статус-код:', r.status_code)

# 2. за допомогою GET отримає посилання на цей файл

url = 'http://127.0.0.1:8080/image/blanc.bmp'

# Виконання GET-запиту для скачування файлу
headers = {'Content-type': 'text'}
response_get = requests.get(url, headers=headers)
with open('Saved/reference.txt', 'wb') as file:
    file.write(response_get.content)

# Перевірка статус-коду
if response_get.status_code == 200:
    created_data = response_get.json()  # отримання даних у форматі JSON
    print('Отримано дані:', created_data)
else:
    print('Get request. Помилка. Статус-код:', response_get.status_code)

# 3. за допомогою DELETE зробить видалення файлу з сервера

url = 'http://127.0.0.1:8080/delete/blanc.bmp'

response_delete = requests.delete(url)
with open('Saved/delete_log.txt', 'wb') as file:
    file.write(response_delete.content)


# Перевірка статус-коду
if response_delete.status_code == 200:
    deleted_data = response_get.json()  # отримання даних у форматі JSON
    print('Отримано дані про видалення:', deleted_data)
else:
    print('Delete request. Помилка. Статус-код:', response_get.status_code)
