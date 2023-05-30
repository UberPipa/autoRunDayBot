import os
import time
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from dotenv import load_dotenv


load_dotenv()
login = os.getenv('LOGIN')
password = os.getenv('PASSWORD')

chrome_driver_path = os.path.dirname(__file__)
chrome_driver_path = os.path.join(chrome_driver_path, 'chromedriver.exe')

# url = 'https://bitrix.stdpr.ru/auth/?login=yes&backurl=%2Fstream%2F'
url = 'https://bitrix.stdpr.ru/'

chrome_options = Options()
chrome_options.add_argument('--headless')


service = Service(chrome_driver_path)
driver = webdriver.Chrome(
    service=service,
    options=chrome_options
)


# def check_status():



try:
    driver.get(url=url)
    time.sleep(0.5)
    name_input = driver.find_element(By.NAME, "USER_LOGIN")
    name_input.send_keys(login)
    pass_input = driver.find_element(By.NAME, 'USER_PASSWORD')
    pass_input.send_keys(password)
    logIn = driver.find_element(By.XPATH, '//*[@id="login-popup"]/div/form/div[2]/input').click()
    time.sleep(0.5)
    close_window = driver.find_element(By.XPATH, '//span[(@class="popup-window-close-icon popup-window-titlebar-close-icon")]').click()
    time.sleep(0.3)
    choice_work_time = driver.find_element(By.XPATH, '//div[(@id="timeman-container")]').click()
    time.sleep(0.3)
    end_work = driver.find_element(By.XPATH, '//div[(@class="tm-popup-button-handler")]').click()
    time.sleep(0.3)
    start_work = driver.find_element(By.XPATH, '//div[(@class="tm-popup-button-handler")]').click()
    time.sleep(0.3)
    print('Готово')


except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()


