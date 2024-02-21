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



driver.get("https://demoqa.com/sortable")

SOURCE_LOCATOR = ("xpath", "//div[contains(@class, 'vertical-list')]/div[1]")
TARGET_LOCATOR = ("xpath", "//div[contains(@class, 'vertical-list')]/div[5]")

def drag_and_drop(source, target):
    SOURCE = driver.find_element(*source) # Находим source-элемент
    TARGET = driver.find_element(*target) # Находим target-элемент
    wait.until(EC.element_to_be_clickable(SOURCE)) # Ждем кликабельности source-элемента
    action.drag_and_drop(SOURCE, TARGET).perform() # Перетаскиваем

drag_and_drop(SOURCE_LOCATOR, TARGET_LOCATOR)