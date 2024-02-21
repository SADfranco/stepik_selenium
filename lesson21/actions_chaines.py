import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--window-size=1920,1080")

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)
wait = WebDriverWait(driver, 10, poll_frequency=1) # Создаем обьект ожиданий
action = ActionChains(driver) # Создаем обьект action


driver.get("https://demoqa.com/buttons")

DB_BUTTON_LOCATOR = ("xpath", "//button[@id='doubleClickBtn']")
RС_BUTTON_LOCATOR = ("xpath", "//button[@id='rightClickBtn']")

DC_BUTTON = driver.find_element(*DB_BUTTON_LOCATOR)
RC_BUTTON = driver.find_element(*RС_BUTTON_LOCATOR)

action.double_click(DC_BUTTON).pause(2).context_click(RC_BUTTON).perform()

time.sleep(2)