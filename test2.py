# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By
# import requests
# from data import linkLogIn, dataFormAuth, main_page, headear
#
#
# def startEndDay():
#     try:
#         # driver.implicitly_wait(10)
#         session = requests.Session()
#         session.post(linkLogIn, data=dataFormAuth, headers=headear)
#         chrome_options = Options()
#         # Делаем запуск скрытным
#         chrome_options.add_argument('--headless')
#         driver = webdriver.Chrome(options=chrome_options)
#         # Устанавливает максимальное время на загрузку страницы
#         # Забираем куки из сессии
#         cookies = session.cookies.get_dict()
#         driver.get(main_page)
#         # Раскидываем куки
#         for name, value in cookies.items():
#             driver.add_cookie({'name': name, 'value': value})
#         # Переходим на главную страницу
#         driver.get(url=main_page)
#         # закрываем вслывающее окно
#         driver.find_element(By.XPATH, '//span[(@class="popup-window-close-icon popup-window-titlebar-close-icon")]').click()
#         # выбиваем меню статуса работника
#         driver.find_element(By.XPATH, '//div[(@id="timeman-container")]').click()
#         # жмякаем на кнопку start/end рабочее время
#         driver.find_element(By.XPATH, '//div[(@class="tm-popup-button-handler")]').click()
#         # driver.quit()
#         driver.close()
#         return True
#     except Exception as ex:
#         print(ex)
#         return False
