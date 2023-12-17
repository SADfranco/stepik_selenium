import time
from bs4 import BeautifulSoup
from main import attribute

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://ya.ru")
text_field = driver.find_element("xpath", "//input[@id='text']")
assert text_field.get_attribute("value") == ""

text_field.send_keys("погода")
attribute(text_field)

#assert text_field.get_attribute("value") == "погода"
#time.sleep(3)
#
#button = driver.find_element("xpath", "//div//li[@data-text = 'погода в москве']")
#button.click()
#
#time.sleep(5)