import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://www.wikipedia.org/") # Переход по ссылке

url = driver.current_url # Получение ссылки страницы
print("URL Страницы: ", url) # Печатаем ссылку страницы
assert url == "https://www.wikipedia.org/", "Ошибка в URL" # Проверяем на той ли мы странице, если нет - выводим ошибку


current_title = driver.title # Получение title страницы
print("title Страницы:", current_title) # Печатаем title страницы
assert current_title == "Wikipedia", "Ошибка в title" #  Проверяем title страницы

print(driver.page_source) # Печатаем html код страницы

time.sleep(3) # Задержка действия