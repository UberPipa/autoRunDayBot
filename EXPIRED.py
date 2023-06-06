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
    "TYPE": "AUTH",
    "backurl": "/",
    f"USER_LOGIN": login,
    f"USER_PASSWORD": password,
}

session.post(
    'https://bitrix.stdpr.ru/?login=yes',
    headers=headers,
    data={
        "AUTH_FORM": "Y",
        "TYPE": "AUTH",
        "backurl": "/",
        f"USER_LOGIN": login,
        f"USER_PASSWORD": password,
    }
)

get_csrf = session.post(
    'https://bitrix.stdpr.ru/bitrix/services/main/ajax.php?action=bitrix%3Atimeman.api.monitor.isAvailable',
    headers=headers
)
csrf = get_csrf.headers.get(
    'X-Bitrix-New-Csrf'
)

get_update = session.post(
    "https://bitrix.stdpr.ru/bitrix/tools/timeman.php",
    data={
        "action": "update",
        "site_id": "s1",
        "sessid": csrf,
    },
    params={
        "device": "browser",
    }
)

status = get_update.text
####### Возможно можно убрать получение часов
get_clock = session.post(
    "https://bitrix.stdpr.ru/bitrix/tools/timeman.php",
    data={
        "action": "clock",
        "start_time": "64800",
        "clock_id": "timeman_report_clock",
        "sessid": csrf,
    },
    params={
        "device": "browser",
    }
)
####### Завершение для. timestamp  это время завершения по unix времени, начинаетя с 00:00  64800 - 18 часов. 60s * 60min = 3600 * 18
time_close = '68400'
report = 'Забыл завершить день.'

close_last_day = session.post(
    "https://bitrix.stdpr.ru/bitrix/tools/timeman.php",
    data={
        "timestamp": time_close,
        "report": report,
        "device": "browser",
    },
    params={
        "action": "close",
        "site_id": "s1",
        "sessid": csrf,
    }
)




cookies = session.cookies.get_dict()
print(close_last_day.headers)
print(' ')
print(cookies)
