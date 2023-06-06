import os
from dotenv import load_dotenv
import requests
import fake_useragent


session = requests.Session()

load_dotenv()
login = os.getenv('LOGIN')
password = os.getenv('PASSWORD')

user = fake_useragent.UserAgent().random
headers = {
    'User-Agent': user,
}

data = {
    "AUTH_FORM": "Y",
    "TYPE":	"AUTH",
    "backurl":	"/",
    f"USER_LOGIN":	login,
    f"USER_PASSWORD":	password,
}
### 1
auth = session.post('https://bitrix.stdpr.ru/?login=yes', headers=headers, data=data)


#get_tineman = session.post('https://bitrix.stdpr.ru/bitrix/services/main/ajax.php?action=bitrix%3Atimeman.api.monitor.isAvailable', headers=headers)
### 2
get_csrf = session.post('https://bitrix.stdpr.ru/bitrix/services/main/ajax.php?action=bitrix%3Atimeman.api.monitor.isEnableForCurrentUser', headers=headers)
csrf = get_csrf.headers.get('X-Bitrix-New-Csrf')


data = {
    "timestamp": "0",
    "report": "",
    "device": "browser",
}

params = {
    "action": "open",
    "site_id": "s1",
    "sessid": csrf,
}



### 3
open = session.post('https://bitrix.stdpr.ru/bitrix/tools/timeman.php', headers=headers, data=data, params=params)


cookies = session.cookies.get_dict()
print(open.request.url)
print(' ')
print(open.headers)
print(' ')
print(cookies)
print(csrf)



