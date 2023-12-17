import time
from bs4 import BeautifulSoup
from main import attribute

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://the-internet.herokuapp.com/status_codes")

driver.find_element("xpath", "//a[@href='status_codes/200']").click()
if driver.current_url == 'https://the-internet.herokuapp.com/status_codes/200':
    print("Страница с 200 кодами")
else:
    print(driver.current_url)

driver.back()

driver.find_element("xpath", "//a[@href='status_codes/301']").click()
assert driver.current_url == 'https://the-internet.herokuapp.com/status_codes/301'

driver.back()

driver.find_element("xpath", "//a[@href='status_codes/404']").click()
assert driver.current_url == 'https://the-internet.herokuapp.com/status_codes/404'

driver.back()

driver.find_element("xpath", "//a[@href='status_codes/500']").click()
assert driver.current_url == 'https://the-internet.herokuapp.com/status_codes/500'

driver.back()

assert driver.current_url == "https://the-internet.herokuapp.com/status_codes"