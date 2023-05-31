import os
import time
import fake_useragent
import requests
from dotenv import load_dotenv
from selenium import webdriver

load_dotenv()
login = os.getenv('LOGIN')
password = os.getenv('PASSWORD')


session = requests.Session()
user = fake_useragent.UserAgent().random
headear = {
    'User-Agent': user
}
url = 'https://bitrix.stdpr.ru/auth/?login=yes&backurl=%2Fstream%2F'
data = {
    'AUTH_FORM': 'Y',
    'TYPE': 'AUTH',
    'backurl': '/auth/?backurl=%2Fstream%2F',
    'USER_LOGIN': login,
    'USER_PASSWORD': password
}
resource = session.post(url, data=data, headers=headear)

main_page = 'https://bitrix.stdpr.ru/stream/'
###
cookies = session.cookies.get_dict()
options = webdriver.ChromeOptions()

driver = webdriver.Chrome(options=options)
driver.get(main_page)
time.sleep(3)
for name, value in cookies.items():
    driver.add_cookie({'name': name, 'value': value})
time.sleep(1)
driver.get(main_page)
time.sleep(3)



