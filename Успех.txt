import os
from dotenv import load_dotenv
import requests
import fake_useragent
import execjs

session = requests.Session()

load_dotenv()
login = os.getenv('LOGIN')
password = os.getenv('PASSWORD')

user = fake_useragent.UserAgent().random
headers_start = {
    'User-Agent': user,
}
start_page = session.get(
    'https://bitrix.stdpr.ru/',
    headers=headers_start,
    allow_redirects=True
)

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

auth = session.post('https://bitrix.stdpr.ru/?login=yes', headers=headers, data=data)
###

#get_tineman = session.post('https://bitrix.stdpr.ru/bitrix/services/main/ajax.php?action=bitrix%3Atimeman.api.monitor.isAvailable', headers=headers)
get_csrf = session.post('https://bitrix.stdpr.ru/bitrix/services/main/ajax.php?action=bitrix%3Atimeman.api.monitor.isEnableForCurrentUser', headers=headers)
csrf = get_csrf.headers.get('X-Bitrix-New-Csrf')


data = {
    "action": "reopen",
    "site_id": "s1",
    "sessid": csrf,
}
headers = {
    'User-Agent': user,
}


get_reopen = session.post('https://bitrix.stdpr.ru/bitrix/tools/timeman.php', headers=headers, data=data)
#get_close = session.post('https://bitrix.stdpr.ru/bitrix/tools/timeman.php?action=close&site_id=s1&sessid=4be8654e9e1dc337cb52927b2fe106a8', headers=headers)

cookies = session.cookies.get_dict()
print(auth.request.url)
print(' ')
print(get_reopen.text)
print(' ')
print(cookies)





# headers_get_scripts = {
#     'User-Agent': user,
#     'Accept': '*/*',
#     'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
#     'Connection': 'keep-alive',
#     'Referer': 'https://bitrix.stdpr.ru/',
#     'Sec-Fetch-Dest': 'script',
#     'Sec-Fetch-Mode': 'no-cors',
#     'Sec-Fetch-Site': 'same-origin',
# }
#
# get_core = session.get(
#     'https://bitrix.stdpr.ru/bitrix/js/main/core/core.min.js?1639581579262092',
#     headers=headers_get_scripts,
# )
# get_kernel = session.get(
#     'https://bitrix.stdpr.ru/bitrix/cache/js/s1/login/kernel_main/kernel_main_v1.js?1651822575197411',
#     headers=headers_get_scripts,
# )
# get_protobuf = session.get(
#     'https://bitrix.stdpr.ru/bitrix/js/pull/protobuf/protobuf.min.js?161849461676433',
#     headers=headers_get_scripts,
# )
# get_model = session.get(
#     'https://bitrix.stdpr.ru/bitrix/js/pull/protobuf/model.min.js?161849461614190',
#     headers=headers_get_scripts,
# )
# get_rest = session.get(
#     'https://bitrix.stdpr.ru/bitrix/js/rest/client/rest.client.min.js?16184946169240',
#     headers=headers_get_scripts,
# )
# get_pull = session.get(
#     'https://bitrix.stdpr.ru/bitrix/js/pull/client/pull.client.min.js?163342716044687',
#     headers=headers_get_scripts,
# )
# get_popup = session.get(
#     'https://bitrix.stdpr.ru/bitrix/js/main/popup/dist/main.popup.bundle.min.js?163958157962522',
#     headers=headers_get_scripts,
# )
# get_template = session.get(
#     'https://bitrix.stdpr.ru/bitrix/cache/js/s1/login/template_fd582a7d79d90c89dd607cb856cc84ba/template_fd582a7d79d90c89dd607cb856cc84ba_v1.js?164477899714751',    headers=headers_get_scripts,
# )
#
# headers_get_ajax_counter = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/113.0',
#     'Accept': '*/*',
#     'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
#     'Content-type': 'application/x-www-form-urlencoded',
#     'Origin': 'https://bitrix.stdpr.ru',
#     'Connection': 'keep-alive',
#     'Referer': 'https://bitrix.stdpr.ru/',
#     'Sec-Fetch-Dest': 'empty',
#     'Sec-Fetch-Mode': 'cors',
#     'Sec-Fetch-Site': 'same-origin',
# }
#
#
# data = {
#     'SITE_ID': 's1',
#     'sessid': 'bd368a6f006c749a0ca76e63709bf058',
#     'HTTP_REFERER': '',
# }
#
#
#
# get_ajax_counter = session.get(
#     'https://bitrix.stdpr.ru/bitrix/tools/conversion/ajax_counter.php',
#     headers=headers_get_ajax_counter,
# )
# cookies = session.cookies.get_dict()






