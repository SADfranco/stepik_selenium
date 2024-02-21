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



driver.get("https://demoqa.com/radio-button")

YES_RADIO_BUTTON = ("xpath", "//input[@id='yesRadio']")
IMPRESSIVE_RADIO_BUTTON = ("xpath", "//input[@id='impressiveRadio']")
NO_RADIO_BUTTON = ("xpath", "//input[@id='noRadio']")

assert driver.find_element(*NO_RADIO_BUTTON).is_enabled() is False, "Кнопка доступна"

YES_RADIO_BUTTON = ("xpath", "//input[@id='yesRadio']") # Для статуса
YES_RADIO_LABEL = ("xpath", "//label[@for='yesRadio']") # Для взаимодействия

driver.find_element(*YES_RADIO_LABEL).click()

assert driver.find_element(*YES_RADIO_BUTTON).is_selected() is True, "Радио-кнопка не выбрана"