import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 15, poll_frequency=1)

driver.get("https://chercher.tech/practice/explicit-wait-sample-selenium-webdriver")


##1.Кликнуть на кнопку “Change Text to Selenium Webdriver” и дождаться изменения текста элемента рядом
#
#button = ('xpath', '//button[@id="populate-text"]')
#text = ('xpath', '//h2[@class="target-text"]')
#
#wait.until(EC.visibility_of_element_located(button)).click()
#wait.until(EC.text_to_be_present_in_element(text, 'Selenium Webdriver'))
#
#assert 'Selenium Webdriver' in driver.find_element(*text).text
#
##2.Кликнуть на кнопку “Display button after 10 seconds” и дождаться появления кнопки “Enabled”
#
#button = ('xpath', '//button[@id="display-other-button"]')
#button_enabled = ('xpath', '//button[@id="hidden"]')
#
#wait.until(EC.visibility_of_element_located(button)).click()
#wait.until(EC.visibility_of_element_located(button_enabled)).click()
#
#assert driver.find_element(*button_enabled).is_displayed()
#
##3.Кликнуть на кнопку “Enable button after 10 seconds" и дождаться кликабельности кнопки “Button”
#
#
#button = ('xpath', '//button[@id="enable-button"]')
#button_click = ('xpath', '//button[@id="disable"]')
#
#wait.until(EC.visibility_of_element_located(button)).click()
#wait.until(EC.element_to_be_clickable(button_click)).click()
#
#assert driver.find_element(*button_click).is_enabled()

#4.Кликнуть на кнопку “Click me, to Open an alert after 5 seconds” и дождаться открытия алерта

button = ('xpath', '//button[@id="alert"]')

wait.until(EC.visibility_of_element_located(button)).click()
wait.until(EC.alert_is_present())
time.sleep(2)
driver.switch_to_alert().accept()

time.sleep(2)