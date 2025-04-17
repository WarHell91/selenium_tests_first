import os
import time    # Импортируем необходимый стек из библиотеки

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

chrome_options = webdriver.ChromeOptions()
prefs = {
    "download.default_directory": f"{os.getcwd()}/downloads" # Путь для скачивания файла ({os.getcwd()}"где лежит код")
}
chrome_options.add_experimental_option("prefs", prefs) # Используем наш словарь
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get("https://www.lada.ru/cars/new-largus/cross")

time.sleep(3)

driver.find_element("xpath", "//a[text()='Скачать прайс-лист']").click()

time.sleep(10)