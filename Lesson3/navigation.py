import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://ya.ru")
title = driver.title
print(f"Текущий заголовок страницы: {title}")

time.sleep(3)

driver.get("https://dzen.ru")
title1 = driver.title
print(f"Текущий заголовок страницы: {title1}")

time.sleep(3)

driver.back()
assert title == "Яндекс", "Заголовок не верный"

driver.refresh()
time.sleep(3)

url = driver.current_url
print(f"Текущий url страницы: {url}")

time.sleep(3)
driver.forward()
url1 = driver.current_url
assert url1 == url, "Верный url"


