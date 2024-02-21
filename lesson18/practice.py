import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver import Keys

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 10, poll_frequency=1)

driver.get("https://hyperskill.org/login")
driver.switch_to.new_window("tab")
driver.get("https://www.avito.ru/")
driver.switch_to.new_window("tab")
driver.get("https://www.ozon.ru/")

windows = driver.window_handles


driver.switch_to.window(windows[0])
title_1 = driver.title

driver.switch_to.window(windows[1])
title_2 = driver.title

driver.switch_to.window(windows[2])
title_3 = driver.title

print(title_1)
print(title_2)
print(title_3)

driver.switch_to.window(windows[0])
driver.find_element('xpath', '//li[@click-event-target="join_as_organization"]').click()
time.sleep(2)
driver.close()

driver.switch_to.window(windows[1])
driver.find_element('xpath', '//a[@class="index-nav-link-muv1u"]').click()
time.sleep(2)
driver.close()

driver.switch_to.window(windows[2])
driver.find_element('xpath', '//a[@class="a1j du4 d4u"]').click()
time.sleep(2)
