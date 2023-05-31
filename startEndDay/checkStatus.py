from typing import Union

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import requests
from data import linkLogIn, dataFormAuth, main_page, headear


def checkStatus() -> Union[str, bool]:
    try:
        session = requests.Session()
        session.post(linkLogIn, data=dataFormAuth, headers=headear)
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        driver = webdriver.Chrome(options=chrome_options)
        # driver.implicitly_wait(10)
        cookies = session.cookies.get_dict()
        driver.get(main_page)
        for name, value in cookies.items():
            driver.add_cookie({'name': name, 'value': value})
        driver.get(url=main_page)
        driver.find_element(By.XPATH, '//span[(@class="popup-window-close-icon popup-window-titlebar-close-icon")]').click()
        try:
            if driver.find_element(By.XPATH, "//span[text()='Работаю']"):
                print('Работаешь')
                return 'Работаешь'
        except Exception:
            pass
        try:
            if driver.find_element(By.XPATH, "//span[text()='Завершен']"):
                return 'Завершен'
        except Exception:
            pass
        try:
            if driver.find_element(By.XPATH, "//span[text()='Перерыв']"):
                return 'Перерыв'
        except Exception:
            pass
    except Exception:
        pass

checkStatus()
