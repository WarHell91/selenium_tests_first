import time    # Импортируем необходимый стек из библиотеки

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

chrome_options = webdriver.ChromeOptions() # Добавить опции браузера (Например: Без UI, инкогнито и т.д.)

chrome_options.page_load_strategy = "normal" # Скорость загрузки страницы (Бывает еще eager(Не дожидается прогрузки всех попапов и т.д.))
chrome_options.add_argument("--headless") # Отключить UI браузера
chrome_options.add_argument("--incognito") # Запустить тест в режиме инкогнито
chrome_options.add_argument("--ignore-certificate-errors") # Игнорировать ССЛ сертификат
chrome_options.add_argument("--window-size=1920,1080") # Запустить окно в определенном разрешении (Желательно использовать этот метод)
chrome_options.add_argument("--disable-cash") # Не будет записываться кеш

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)
#driver.set_window_size(1920, 1080)  # Команда делает тоже самое что и chrome_options.add_argument("--window-size=700,700"), только через драйвер

stat_time = time.time() # Записываем начальное время

driver.get("https://whatismyipaddress.com/")

end_time = time.time() # Записываем конечное время

result = end_time - stat_time # Определяем разницу между начальным и конечным временем

print(result) # Выводим результат