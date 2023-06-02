from selenium import webdriver

# Создаем экземпляр драйвера Chrome
driver = webdriver.Chrome()

# Загружаем страницу
driver.get("https://bitrix.stdpr.ru/")

# Получаем объект документа (document)
document = driver.execute_script("return document")

# Выводим содержимое документа на экран
print(document)

# Закрываем браузер
driver.quit()