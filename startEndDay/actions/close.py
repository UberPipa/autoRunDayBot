import os
from dotenv import load_dotenv
import requests
import fake_useragent
from startEndDay.actions.siteFunctions import login_user

session = requests.Session()
session, headers = login_user(session)


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
print(get_close.request.url)
print(' ')
print(get_close.text)
print(' ')
print(cookies)
print(csrf)




