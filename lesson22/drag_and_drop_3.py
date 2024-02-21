import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains


service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 10, poll_frequency=1)
action = ActionChains(driver)

driver.get("https://tympanus.net/Development/DragDropInteractions/index.html")

source = driver.find_element("xpath", "//div[@class='grid__item'][7]") # Что перетаскиваем
target = driver.find_element("xpath", "//div[@class='drop-area__item'][2]") # Куда перетаскиваем

action.click_and_hold(source) \
    .pause(2) \
    .move_to_element(target) \
    .release() \
    .perform()

time.sleep(5)
