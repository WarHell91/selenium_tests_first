import time    # Импортируем необходимый стек из библиотеки

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By # Импортируем из бибблиотеки By

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://www.freeconferencecall.com/login") # Ищем страничку

driver.find_element(By.ID,"loginformsubmit").click() # Ищем элемент по ID и кликаем на него

time.sleep(5) # Задержка 5сек

