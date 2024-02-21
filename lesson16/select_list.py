import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

options = Options()
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--user-agent=Automation QA (Windows NT 6.1; rv:106.0) Gecko/20100101 Firefox/106.0")
options.page_load_strategy = "normal"

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)
wait = WebDriverWait(driver, 10, poll_frequency=1)

driver.get("http://the-internet.herokuapp.com/dropdown")

DROPDOWN_ELEMENT = ("xpath", "//select[@id='dropdown']")
DROPDOWN = Select(driver.find_element(*DROPDOWN_ELEMENT))


DROPDOWN.select_by_visible_text("Option 2")
time.sleep(2)
assert driver.find_element('xpath', '//option[@value="2"]').is_selected(), "Не выбрано значение"

DROPDOWN.select_by_index(1)
time.sleep(2)
DROPDOWN.select_by_value("2")
time.sleep(2)

all_options = DROPDOWN.options # Запишем все элементы выпадающего списка
del all_options[0] # ��даляем первый элемент

for option in all_options: # Перебор элементов по тексту
    time.sleep(1)
    DROPDOWN.select_by_visible_text(f"{option.text}")

for option in all_options: # Перебор элементов по value
    time.sleep(1)
    DROPDOWN.select_by_value(option.get_attribute("value"))