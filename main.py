import requests
import fake_useragent
from bs4 import BeautifulSoup

session = requests.Session()

url = 'https://bitrix.stdpr.ru/auth/?login=yes&backurl=%2Fstream%2F'
user = fake_useragent.UserAgent().random

header = {
    'user-agent': user
}

data = {
    "USER_LOGIN": "Privalov@stdpr.ru",
    "USER_PASSWORD": "22tatara"
}

response = session.post(url, data=data, headers=header).text

print(response)






