import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

options = Options()
options.add_argument('--window-size=1920,1080')
#options.add_argument("--disable-blink-features=AutomationControlled")
#options.add_argument("--user-agent=Automation QA (Windows NT 6.1; rv:106.0) Gecko/20100101 Firefox/106.0")
options.page_load_strategy = "normal"

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)
wait = WebDriverWait(driver, 10, poll_frequency=1)


driver.get("https://demoqa.com/select-menu")

driver.find_element("xpath", "//div[@id='withOptGroup']").click()# Открываем dropdown
time.sleep(2)

expext_selection = "Another root option"

driver.find_element("xpath", "//input[@id='react-select-2-input']").send_keys(expext_selection)# Ввести текст

time.sleep(2)
def choose_dropwdown_element_by_text(x): # Будем искать элемент внутри dropdown по тексту
    elements = driver.find_elements("xpath", "//div[@id='withOptGroup']//div[contains(@id, 'react-select')]")
    for element in elements:
        if element.text == x:
            print(element.text)
            return element

choose_dropwdown_element_by_text(expext_selection).click()# Кликаем на выбранный элемент
chosen_option = driver.find_element("xpath", "//div[@id='withOptGroup']")
print("Значение" + chosen_option.text)
assert expext_selection in chosen_option.text, "Не выбрано значение"
time.sleep(2)

#chosen_option = driver.find_element("xpath", "//div[@id='withOptGroup']")
#print("Значение" + chosen_option.text)
#time.sleep(2)

#chosen_option = driver.find_element("xpath", "//p[@id='aria-selection-event']")
#print("Значение" + chosen_option.text)
##assert "A root option" in chosen_option.text, "Не выбрано значение"
#time.sleep(4)

#list_elements = driver.find_elements('xpath', "//div[contains(@id, 'react-select')]")
#for element in list_elements:
#    if element.text == 'Group 1, option 1':
#        print(element.text)
#        wait.until(EC.element_to_be_clickable(element)).click()
#        break
#
#chosen_option = driver.find_element("xpath", "//div[@id='withOptGroup']")
#print("Значение" + chosen_option.text)
#assert "Group 1, option 1" in chosen_option.text, "Не выбрано значение"
#time.sleep(2)

#driver.execute_script('''document.querySelector('div[id="react-select-2-option-1-1"]').click()''') # Один из вариантов выполнения скрипта через Js