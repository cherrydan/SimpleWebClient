import requests


res = requests.get('https://www.avito.ru/web/user/get-status/177068588')

print(res.text)