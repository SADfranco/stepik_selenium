import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(ChromeDriverManager().install())
driver_1 = webdriver.Chrome(service=service)

driver_1.get("https://hyperskill.org/login")
title_1 = driver_1.title

print(title_1)
time.sleep(2)

driver_2 = webdriver.Chrome(service=service)
driver_2.get("https://www.avito.ru/")
title_2 = driver_2.title

print(title_2)

time.sleep(2)