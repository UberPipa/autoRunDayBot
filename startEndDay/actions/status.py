import os
from dotenv import load_dotenv
import requests
import fake_useragent
from startEndDay.actions.siteFunctions import check_status
from startEndDay.data import login, password

session = requests.Session()
session, headers, status, csrf = check_status(session, login, password)







cookies = session.cookies.get_dict()
print(status)
print(' ')
print(cookies)


