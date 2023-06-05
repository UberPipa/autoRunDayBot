import os
from dotenv import load_dotenv
import requests
import fake_useragent
from startEndDay.actions.siteFunctions import login_user, get_status


session = requests.Session()
session, headers, status, csrf = get_status(session)







cookies = session.cookies.get_dict()
print(status)
print(' ')
print(cookies)


