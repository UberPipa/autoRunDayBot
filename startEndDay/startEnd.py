import os
import fake_useragent
import requests
from dotenv import load_dotenv
from startEndDay.data import dataFormAuth, params, linkLogIn, headers, main_page

session = requests.Session()

""" Авторизация """
auth = session.post(
    linkLogIn,
    headers=headers,
    data=dataFormAuth
)


main = session.get('https://bitrix.stdpr.ru/', headers=headers)



cookies = session.cookies.get_dict()


print(main.text)
print(cookies)


###
# cookies = {
#     'PHPSESSID': 't6u37BeSsejyL6mVBPXwvltpFO1tJ401',
#     'BITRIX_CONVERSION_CONTEXT_s1': '^%^7B^%^22ID^%^22^%^3A4^%^2C^%^22EXPIRE^%^22^%^3A1685653140^%^2C^%^22UNIQUE^%^22^%^3A^%^5B^%^22conversion_visit_day^%^22^%^5D^%^7D',
#     'BITRIX_SM_SALE_UID': '0',
#     'BITRIX_SM_LOGIN': 'Privalov^%^40stdpr.ru',
#     'BITRIX_SM_SOUND_LOGIN_PLAYED': 'Y',
#     'BITRIX_SM_TIMEMAN_LAST_PAUSE_1969': '1685623629^%^7C1685623768',
# }
#
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/113.0',
#     'Accept': '*/*',
#     'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
#     # 'Accept-Encoding': 'gzip, deflate, br',
#     'Bx-ajax': 'true',
#     'Content-Type': 'application/x-www-form-urlencoded',
#     'X-Bitrix-Csrf-Token': '454792effb38485662be99c8d99fb323',
#     'X-Bitrix-Site-Id': 's1',
#     # 'Content-Length': '0',
#     'Origin': 'https://bitrix.stdpr.ru',
#     'Connection': 'keep-alive',
#     'Referer': 'https://bitrix.stdpr.ru/stream/',
#     # 'Cookie': 'PHPSESSID=t6u37BeSsejyL6mVBPXwvltpFO1tJ401; BITRIX_CONVERSION_CONTEXT_s1=^%^7B^%^22ID^%^22^%^3A4^%^2C^%^22EXPIRE^%^22^%^3A1685653140^%^2C^%^22UNIQUE^%^22^%^3A^%^5B^%^22conversion_visit_day^%^22^%^5D^%^7D; BITRIX_SM_SALE_UID=0; BITRIX_SM_LOGIN=Privalov^%^40stdpr.ru; BITRIX_SM_SOUND_LOGIN_PLAYED=Y; BITRIX_SM_TIMEMAN_LAST_PAUSE_1969=1685623629^%^7C1685623768',
#     'Sec-Fetch-Dest': 'empty',
#     'Sec-Fetch-Mode': 'cors',
#     'Sec-Fetch-Site': 'same-origin',
#     # Requests doesn't support trailers
#     # 'TE': 'trailers',
# }
#
# response = requests.post(
#     'https://bitrix.stdpr.ru/bitrix/services/main/ajax.php?action=bitrix^%^3Atimeman.api.monitor.isAvailable',
#     cookies=cookies,
#     headers=headers,
# )
# ###
# cookies = {
#     'PHPSESSID': 't6u37BeSsejyL6mVBPXwvltpFO1tJ401',
#     'BITRIX_CONVERSION_CONTEXT_s1': '^%^7B^%^22ID^%^22^%^3A4^%^2C^%^22EXPIRE^%^22^%^3A1685653140^%^2C^%^22UNIQUE^%^22^%^3A^%^5B^%^22conversion_visit_day^%^22^%^5D^%^7D',
#     'BITRIX_SM_SALE_UID': '0',
#     'BITRIX_SM_LOGIN': 'Privalov^%^40stdpr.ru',
#     'BITRIX_SM_SOUND_LOGIN_PLAYED': 'Y',
#     'BITRIX_SM_TIMEMAN_LAST_PAUSE_1969': '1685623629^%^7C1685623768',
# }
#
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/113.0',
#     'Accept': '*/*',
#     'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
#     # 'Accept-Encoding': 'gzip, deflate, br',
#     'Bx-ajax': 'true',
#     'Content-Type': 'application/x-www-form-urlencoded',
#     'Origin': 'https://bitrix.stdpr.ru',
#     'Connection': 'keep-alive',
#     'Referer': 'https://bitrix.stdpr.ru/stream/',
#     # 'Cookie': 'PHPSESSID=t6u37BeSsejyL6mVBPXwvltpFO1tJ401; BITRIX_CONVERSION_CONTEXT_s1=^%^7B^%^22ID^%^22^%^3A4^%^2C^%^22EXPIRE^%^22^%^3A1685653140^%^2C^%^22UNIQUE^%^22^%^3A^%^5B^%^22conversion_visit_day^%^22^%^5D^%^7D; BITRIX_SM_SALE_UID=0; BITRIX_SM_LOGIN=Privalov^%^40stdpr.ru; BITRIX_SM_SOUND_LOGIN_PLAYED=Y; BITRIX_SM_TIMEMAN_LAST_PAUSE_1969=1685623629^%^7C1685623768',
#     'Sec-Fetch-Dest': 'empty',
#     'Sec-Fetch-Mode': 'cors',
#     'Sec-Fetch-Site': 'same-origin',
#     # Requests doesn't support trailers
#     # 'TE': 'trailers',
# }
#
# params = {
#     'action': 'update',
#     'site_id': 's1',
#     'sessid': '454792effb38485662be99c8d99fb323',
# }
#
# data = {
#     'device': 'browser',
# }
#
# response = requests.post(
#     'https://bitrix.stdpr.ru/bitrix/tools/timeman.php',
#     params=params,
#     cookies=cookies,
#     headers=headers,
#     data=data,
# )
# ###
# cookies = {
#     'PHPSESSID': 't6u37BeSsejyL6mVBPXwvltpFO1tJ401',
#     'BITRIX_CONVERSION_CONTEXT_s1': '^%^7B^%^22ID^%^22^%^3A4^%^2C^%^22EXPIRE^%^22^%^3A1685653140^%^2C^%^22UNIQUE^%^22^%^3A^%^5B^%^22conversion_visit_day^%^22^%^5D^%^7D',
#     'BITRIX_SM_SALE_UID': '0',
#     'BITRIX_SM_LOGIN': 'Privalov^%^40stdpr.ru',
#     'BITRIX_SM_SOUND_LOGIN_PLAYED': 'Y',
#     'BITRIX_SM_TIMEMAN_LAST_PAUSE_1969': '1685623629^%^7C1685623768',
# }
#
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/113.0',
#     'Accept': '*/*',
#     'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
#     # 'Accept-Encoding': 'gzip, deflate, br',
#     'Bx-ajax': 'true',
#     'Content-Type': 'application/x-www-form-urlencoded',
#     'X-Bitrix-Csrf-Token': '454792effb38485662be99c8d99fb323',
#     'X-Bitrix-Site-Id': 's1',
#     # 'Content-Length': '0',
#     'Origin': 'https://bitrix.stdpr.ru',
#     'Connection': 'keep-alive',
#     'Referer': 'https://bitrix.stdpr.ru/stream/',
#     # 'Cookie': 'PHPSESSID=t6u37BeSsejyL6mVBPXwvltpFO1tJ401; BITRIX_CONVERSION_CONTEXT_s1=^%^7B^%^22ID^%^22^%^3A4^%^2C^%^22EXPIRE^%^22^%^3A1685653140^%^2C^%^22UNIQUE^%^22^%^3A^%^5B^%^22conversion_visit_day^%^22^%^5D^%^7D; BITRIX_SM_SALE_UID=0; BITRIX_SM_LOGIN=Privalov^%^40stdpr.ru; BITRIX_SM_SOUND_LOGIN_PLAYED=Y; BITRIX_SM_TIMEMAN_LAST_PAUSE_1969=1685623629^%^7C1685623768',
#     'Sec-Fetch-Dest': 'empty',
#     'Sec-Fetch-Mode': 'cors',
#     'Sec-Fetch-Site': 'same-origin',
#     # Requests doesn't support trailers
#     # 'TE': 'trailers',
# }
#
# response = requests.post(
#     'https://bitrix.stdpr.ru/bitrix/services/main/ajax.php?action=bitrix^%^3Atimeman.api.monitor.isEnableForCurrentUser',
#     cookies=cookies,
#     headers=headers,
# )
# ###
# cookies = {
#     'PHPSESSID': 't6u37BeSsejyL6mVBPXwvltpFO1tJ401',
#     'BITRIX_CONVERSION_CONTEXT_s1': '^%^7B^%^22ID^%^22^%^3A4^%^2C^%^22EXPIRE^%^22^%^3A1685653140^%^2C^%^22UNIQUE^%^22^%^3A^%^5B^%^22conversion_visit_day^%^22^%^5D^%^7D',
#     'BITRIX_SM_SALE_UID': '0',
#     'BITRIX_SM_LOGIN': 'Privalov^%^40stdpr.ru',
#     'BITRIX_SM_SOUND_LOGIN_PLAYED': 'Y',
#     'BITRIX_SM_TIMEMAN_LAST_PAUSE_1969': '1685623629^%^7C1685623768',
# }
#
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/113.0',
#     'Accept': '*/*',
#     'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
#     # 'Accept-Encoding': 'gzip, deflate, br',
#     'Bx-ajax': 'true',
#     'Content-Type': 'application/x-www-form-urlencoded',
#     'Origin': 'https://bitrix.stdpr.ru',
#     'Connection': 'keep-alive',
#     'Referer': 'https://bitrix.stdpr.ru/stream/',
#     # 'Cookie': 'PHPSESSID=t6u37BeSsejyL6mVBPXwvltpFO1tJ401; BITRIX_CONVERSION_CONTEXT_s1=^%^7B^%^22ID^%^22^%^3A4^%^2C^%^22EXPIRE^%^22^%^3A1685653140^%^2C^%^22UNIQUE^%^22^%^3A^%^5B^%^22conversion_visit_day^%^22^%^5D^%^7D; BITRIX_SM_SALE_UID=0; BITRIX_SM_LOGIN=Privalov^%^40stdpr.ru; BITRIX_SM_SOUND_LOGIN_PLAYED=Y; BITRIX_SM_TIMEMAN_LAST_PAUSE_1969=1685623629^%^7C1685623768',
#     'Sec-Fetch-Dest': 'empty',
#     'Sec-Fetch-Mode': 'cors',
#     'Sec-Fetch-Site': 'same-origin',
#     # Requests doesn't support trailers
#     # 'TE': 'trailers',
# }
#
# params = {
#     'action': 'close',
#     'site_id': 's1',
#     'sessid': '454792effb38485662be99c8d99fb323',
# }
#
# data = {
#     'timestamp': '0',
#     'report': '',
#     'device': 'browser',
# }
#
# response = requests.post(
#     'https://bitrix.stdpr.ru/bitrix/tools/timeman.php',
#     params=params,
#     cookies=cookies,
#     headers=headers,
#     data=data,
# )
