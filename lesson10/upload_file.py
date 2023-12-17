import os
import time
from bs4 import BeautifulSoup
from main import attribute

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

options = webdriver.ChromeOptions()
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://demoqa.com/automation-practice-form")

upload_file = driver.find_element("xpath" , "//input[@type='file']")
upload_file.send_keys(f'{os.getcwd()}/downloads/460.jpg')
upload_file1 = driver.find_element("xpath" , "//input[@type='file']")

attribute(upload_file1)




