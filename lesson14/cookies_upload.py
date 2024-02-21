import os
import pickle
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
options = webdriver.ChromeOptions()
options.add_argument('--incognito')
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)
wait = WebDriverWait(driver, 10, poll_frequency=1)


driver.get("http://users.bugred.ru/")

print(driver.get_cookie("PHPSESSID"))

driver.delete_cookie("PHPSESSID")

cookies = pickle.load(open(os.getcwd()+"/cookies/cookies.pkl", "rb"))
print(cookies)

driver.add_cookie(cookies)
driver.refresh()
print(driver.get_cookie("PHPSESSID"))
time.sleep(5)