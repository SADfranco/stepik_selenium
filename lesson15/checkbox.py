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


driver.get("http://the-internet.herokuapp.com/checkboxes")


CHECKBOX_1 = ("xpath", "//input[@type='checkbox'][1]")
CHECKBOX_2 = ("xpath", "//input[@type='checkbox'][2]")


driver.find_element(*CHECKBOX_1).click()

assert driver.find_element(*CHECKBOX_1).is_selected() is True

if driver.find_element(*CHECKBOX_1).get_attribute("checked") is not None:
    print("Элемент выбран")

driver.find_element(*CHECKBOX_2).click()

assert driver.find_element(*CHECKBOX_2).is_selected() is False

if driver.find_element(*CHECKBOX_2).get_attribute("checked") is None:
    print("Элемент не выбран")