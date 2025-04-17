import os
import time    # Импортируем необходимый стек из библиотеки

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

chrome_options = webdriver.ChromeOptions()
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get("https://www.lada.ru/cars/new-largus/cross")

time.sleep(3)

driver.find_element("xpath", "//a[text()='Скачать прайс-лист']").send_keys(f"{os.getcwd()}/downloads/2.pdf")

time.sleep(3)