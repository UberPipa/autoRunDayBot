import os
import fake_useragent
from dotenv import load_dotenv


# Запрос серверу на авторизаию
linkLogIn = 'https://bitrix.stdpr.ru/auth/?login=yes&backurl=%2Fstream%2F'

# Загружаем из переменных среды
load_dotenv()
login = os.getenv('LOGIN')
password = os.getenv('PASSWORD')

# Главная страница
main_page = 'https://bitrix.stdpr.ru/stream/'

# Отправляемые данные для авторизации
dataFormAuth = {
    'AUTH_FORM': 'Y',
    'TYPE': 'AUTH',
    'backurl': '/auth/?backurl=%2Fstream%2F',
    'USER_LOGIN': login,
    'USER_PASSWORD': password
}

# Юзер агент
user = fake_useragent.UserAgent().random
headear = {
    'User-Agent': user
}