import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://yandex.ru")

time.sleep(10)

driver.back() # Кнопка назад в браузере

time.sleep(3)

driver.forward() # Кнопка вперед в браузере

time.sleep(3)

driver.refresh() # Кнопка обновить в браузере

time.sleep(3)