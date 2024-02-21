import os
import pickle
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
options = webdriver.ChromeOptions()
#options.add_argument('--incognito')
#options.add_argument('--window-size=1000,760')
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.79 Safari/537.36")

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)
wait = WebDriverWait(driver, 10, poll_frequency=1)

driver.get("https://www.ikea.com/de/de/new/new-products/?filters=f-subcategories%3Awt001")


for i in range(1,5):
    driver.find_element("xpath",f"(//button[contains(@class,'plp-btn--icon-emphasised')])[{i}]").click()

time.sleep(3)

driver.find_element("xpath", "//button[@class='hnf-btn hnf-btn--small hnf-btn--icon-tertiary-inverse']//span[@class='hnf-btn__inner']").click()

#driver.get("https://www.ikea.com/de/de/shoppingcart/")

time.sleep(2)
driver.find_element("xpath", "//button[@id='onetrust-accept-btn-handler']").click()

#scroll to top
driver.execute_script("window.scrollTo(0, document.body.scrollTop)")
#scroll to bottom
#driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")

time.sleep(2)
driver.find_element('xpath','//span[@data-label-default="Warenkorb"]').click()

pickle.dump(driver.get_cookies(), open(os.getcwd() + "/cookies/cookies.pkl", "wb"))
driver.delete_all_cookies()
driver.refresh()

time.sleep(3)
cookies = pickle.load(open(os.getcwd()+"/cookies/cookies.pkl", "rb"))

for cookie in cookies:
    driver.add_cookie(cookie)

driver.refresh()

time.sleep(3)
