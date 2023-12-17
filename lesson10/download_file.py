import os
import time
from bs4 import BeautifulSoup
from main import attribute

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

options = webdriver.ChromeOptions()
prefs = {
    "download.default_directory" : os.getcwd() + "\downloads"
}
options.add_experimental_option("prefs", prefs)
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

driver.get("http://the-internet.herokuapp.com/download")

all_links = driver.find_elements('xpath', '//a[contains(@href, "download/")]')
print(len(all_links))

for i in all_links:
    i.click()

time.sleep(3)

