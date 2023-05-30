import requests
import fake_useragent
from bs4 import BeautifulSoup



url = 'https://bitrix.stdpr.ru/auth/?login=yes&backurl=%2Fstream%2F'

data = {
    "USER_LOGIN": "Privalov@stdpr.ru",
    "USER_PASSWORD": "22tatara"
}

response = requests.post(url, data=data)

print(response.status_code)