import requests

url = "https://geekbrains.ru/lessons/99347"

response = requests.get(url)
print(1)

file = open('post.html', 'w', encoding='UTF-8')
try:
    file.write(response.text)
except IOError:
    pass
finally:
    file.close()
