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


get_csrf = session.post('https://bitrix.stdpr.ru/bitrix/services/main/ajax.php?action=bitrix%3Atimeman.api.monitor.isEnableForCurrentUser', headers=headers)
csrf = get_csrf.headers.get('X-Bitrix-New-Csrf')


params = {
    "timestamp": "0",
    "report": "",
    "device": "browser",
}

data = {
    "action": "close",
    "site_id": "s1",
    "sessid": csrf,
}

### 3
get_close = session.post(f'https://bitrix.stdpr.ru/bitrix/tools/timeman.php', headers=headers, params=params, data=data)


cookies = session.cookies.get_dict()
print(auth.request.url)
print(' ')
print(get_close.text)
print(' ')
print(cookies)
print(csrf)




