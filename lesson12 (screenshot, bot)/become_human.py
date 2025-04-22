import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC # Ожидаемые условия

options = Options()
options.add_argument("--window-size-1920,1080")
options.add_argument("disable-blink-features=AutomationControlled") # Скрываем что мы робот

# Меняем user-agent на тот который нужен
options.add_argument("--user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.3")

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 15, poll_frequency=1)

driver.get("https://www.browserscan.net/ru/bot-detection")
driver.save_screenshot("123.png") # Сделать скриншот страницы

time.sleep(15)


