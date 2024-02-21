import os
import pickle
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
options = webdriver.ChromeOptions()
#options.add_argument('--incognito')
#options.add_argument('--window-size=1000,760')
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.79 Safari/537.36")

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)
wait = WebDriverWait(driver, 10, poll_frequency=1)


driver.get("https://demoqa.com/checkbox")

# Сам чек-бокс для проверки статуса
HOME_CHECKBOX = ("xpath", "//input[@id='tree-node-home']")

# Элемент для клика, чтобы выставить флажок
HOME_BUTTON = ("xpath", "//span[text()='Home']")

# Кликаем на элемент, который выставляет чек-бокс
driver.find_element(*HOME_BUTTON).click()

# Выведем статус чек-бокса, так как он меняется при клике на элемент, отвечающий за выставление флажка
print(driver.find_element(*HOME_CHECKBOX).is_selected())