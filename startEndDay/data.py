import os
import fake_useragent
from dotenv import load_dotenv

# Загружаем из переменных среды
load_dotenv()
login = os.getenv('LOGIN')
password = os.getenv('PASSWORD')


user = fake_useragent.UserAgent().random
headers = {
    'User-Agent': user,
}