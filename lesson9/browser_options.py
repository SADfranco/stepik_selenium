import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

options = webdriver.ChromeOptions()
#options.page_load_strategy = 'eager'
#options.add_argument('--headless')
#options.add_argument('--incognito')
#options.add_argument('--ignore-certificate-errors')
options.add_argument('--window-size=1920,1080')
#options.add_argument('--disable-cache')
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://ya.ru")

time.sleep(3)
