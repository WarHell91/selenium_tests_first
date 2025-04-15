import time    # Импортируем необходимый стек из библиотеки
from symtable import Class

from cffi.cffi_opcode import CLASS_NAME
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By # Импортируем из бибблиотеки By

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://hyperskill.org/courses") # Ищем страничку

time.sleep(3)

driver.find_elements("class name", "nav-link")[2].click() # Ищем элемент по списку [2] и кликаем на него

time.sleep(5)


