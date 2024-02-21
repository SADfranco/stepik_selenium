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


driver.get("https://demoqa.com/droppable")

SOURCE_LOCATOR = ("xpath", "//div[@id='draggable']")
TARGET_LOCATOR = ("xpath", "//div[@id='droppable']")

SOURCE = driver.find_element(*SOURCE_LOCATOR)
TARGET = driver.find_element(*TARGET_LOCATOR)

wait.until(EC.element_to_be_clickable(SOURCE))
action.drag_and_drop(SOURCE, TARGET).perform() # Перетаскивание

time.sleep(5)