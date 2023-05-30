import os
import time
import requests

import requests
from dotenv import load_dotenv
from selenium import webdriver

load_dotenv()
login = os.getenv('LOGIN')
password = os.getenv('PASSWORD')

url = 'https://bitrix.stdpr.ru/auth'
user_agent_val = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'
data = {
    f"AUTH_FORM=Y&TYPE=AUTH&backurl=%2Fauth%2F%3Fbackurl%3D%252Fstream%252F&USER_LOGIN={login}%40stdpr.ru&USER_PASSWORD={password}"
}

# Создаем сессию и указываем ему наш user-agent
session = requests.Session()
r = session.get(url, headers={
    'User-Agent': user_agent_val
})





# with open('test.html', 'w') as w:
#     w.write(req.text)


# response = requests.post(url, data=data)
# cookies = response.cookies.get_dict()
# driver = webdriver.Chrome()
# driver.get('https://bitrix.stdpr.ru/stream/')
# current_domain = driver.current_url.split('/')[2]
#
# for name, value in cookies.items():
#     cookie = {'name': name, 'value': value, 'domain': current_domain}
#     driver.add_cookie(cookie)
#
# # Обновить страницу, чтобы применить куки
# driver.refresh()
# time.sleep(5)
#
