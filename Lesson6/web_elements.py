import time
from bs4 import BeautifulSoup

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://ya.ru")
time.sleep(3)
element = driver.find_element("xpath", "//button[@data-action='voice']")


##find all attributes of current element
#attrs=[]
#for attr in element.get_property('attributes'):
#    attrs.append([attr['name'], attr['value']])
#print(attrs)
