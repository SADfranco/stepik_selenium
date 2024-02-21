import time
from selenium import webdriver

PROXY = "103.133.223.18:8080"  # Указываем адрес прокси-сервера
#PROXY = "username:password@37.19.220.129:8443" Указываем логин и пароль для прокси-сервера

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument(f"--proxy-server={PROXY}")  # Добавляем прокси через опции

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://whatismyipaddress.com/")  # Проверяем IP-адрес

time.sleep(5)