import time
from bs4 import BeautifulSoup
from main import attribute

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://demoqa.com/automation-practice-form")
fname_field = driver.find_element("xpath", "//input[@placeholder='First Name']")
assert fname_field.get_attribute("value") == ""
fname_field.send_keys("Andrei")
assert 'Andrei' in fname_field.get_attribute('value')

lname_field = driver.find_element("xpath", "//input[@placeholder='Last Name']")
lname_field.get_attribute('value')
assert lname_field.get_attribute('value') == ""
lname_field.send_keys("Shabaev")
assert 'Shabaev' in lname_field.get_attribute('value')

time.sleep(2)
lname_field.clear()
assert "" in lname_field.get_attribute('value')
time.sleep(2)

if fname_field.get_attribute('value') != "":
    fname_field.clear()
    fname_field.send_keys("San")
else:
    print('Поле пустое')