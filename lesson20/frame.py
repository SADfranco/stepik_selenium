import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://testautomationpractice.blogspot.com")
iframe_volunteer = driver.find_element('xpath', "//iframe")

driver.switch_to.frame(iframe_volunteer)

first_name_field = driver.find_element('xpath', "//input[@id='RESULT_TextField-0']")
first_name_field.send_keys("Alexey")
time.sleep(3)


driver.switch_to.default_content() # Переключение с iframe обратно на страницу
