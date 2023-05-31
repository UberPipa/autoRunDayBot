from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import requests
from data import linkLogIn, dataFormAuth, main_page, headear


def checkStatus():
    try:
        session = requests.Session()
        session.post(linkLogIn, data=dataFormAuth, headers=headear)
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        driver = webdriver.Chrome(options=chrome_options)
        #driver.implicitly_wait(10)
        cookies = session.cookies.get_dict()
        driver.get(main_page)
        for name, value in cookies.items():
            driver.add_cookie({'name': name, 'value': value})
        driver.get(url=main_page)
        driver.find_element(By.XPATH, '//span[(@class="popup-window-close-icon popup-window-titlebar-close-icon")]').click()
        driver.find_element(By.XPATH, '//div[(@id="timeman-container")]').click()
        try:
            if driver.find_element(By.XPATH, '//button[(@class="ui-btn ui-btn-danger ui-btn-icon-stop")]'):
                print('Есть карасная')
        except Exception as ex:
            pass
        try:
            if driver.find_element(By.XPATH, '//button[(@class="ui-btn ui-btn-success ui-btn-icon-start")]'):
                print('Есть зелёная')
        except Exception as ex:
            pass




        # жмякаем на кнопку start/end рабочее время
        # end_work = driver.find_element(By.XPATH, '//div[(@class="tm-popup-button-handler")]').click()
        # driver.quit()
        # driver.close()
        return True
    except Exception as ex:
        return False

print(checkStatus())


# END
# //*[@id="popup-window-content-timeman_main"]/div/div[2]/table/tbody/tr/td[2]/div
# //*[@id="popup-window-content-timeman_main"]/div/div[2]/table/tbody/tr/td[2]/div/button
# class="ui-btn ui-btn-danger ui-btn-icon-stop"

# START
# //*[@id="popup-window-content-timeman_main"]/div/div[2]/table/tbody/tr/td[2]/div
# //*[@id="popup-window-content-timeman_main"]/div/div[2]/table/tbody/tr/td[2]/div/button
# class="ui-btn ui-btn-success ui-btn-icon-start"
