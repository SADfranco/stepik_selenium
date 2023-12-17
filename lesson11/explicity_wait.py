from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 30, poll_frequency=1)

driver.get("https://demoqa.com/dynamic-properties")

button_visib = ('xpath', '//button[@id="visibleAfter"]')
#visibility_of_element_located(locator) - Ожидание проверки того, что элемент присутствует в DOM и виден визуально. Видимость означает, что элемент не только отображается но также имеет высоту и ширину, которые больше 0.
wait.until(EC.visibility_of_element_located(button_visib)).click()

button_click = ('xpath', '//button[@id="enableAfter"]')
#element_to_be_clickable(locator) - Ожидает видимости элемента и его кликабельности (возможности кликнуть).
wait.until(EC.element_to_be_clickable(button_click)).click()


#invisibility_of_element_located(locator) - Ожидание проверки того, является ли элемент невидимым или он исчез из DOM.
wait.until(EC.invisibility_of_element_located()).click()

#text_to_be_present_in_element(locator, text) - Ожидание наличия нужного текста в элементе.
wait.until(EC.text_to_be_present_in_element()).click()