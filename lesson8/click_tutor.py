import time    # Импортируем необходимый стек из библиотеки

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://www.freeconferencecall.com/ru/ru/login")

login_button = driver.find_element("xpath", "//a[@id='login-desktop']")
login_button.click()

time.sleep(5)

form_button = driver.find_element("xpath", "//button[@type='button' and @id='loginformsubmit']")
form_button.click()

time.sleep(3)

email_field = driver.find_element("xpath", "//input[@id='login_email']") # Ищем элемент, а именно инпут формы
email_field.send_keys("WarHell91@mail.ru") # Ввод текста в форму инпута

time.sleep(3)

email_field.clear()

email_field.send_keys("asdasdasdasdasda")

print(email_field.get_attribute("value")) # Распечатать значение в поле инпута


time.sleep(3)