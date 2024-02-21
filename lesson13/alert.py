import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Создание экземпляра веб-драйвера
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 10, poll_frequency=1)

# Переход на веб-страницу
driver.get("https://demoqa.com/alerts")

# Клик на кнопку, которая вызывает alert
BUTTON_1 = ("xpath", "//button[@id='alertButton']")
wait.until(EC.element_to_be_clickable(BUTTON_1)).click()

# Ожидание появления alert и запись его в переменную для дальнейшего взаимодействия
alert = wait.until(EC.alert_is_present())

# Переключение на alert
driver.switch_to.alert

# Ввод данных в alert
#alert.send_keys("Hello world")

alert.accept() # Принимаем алерт
#alert.dismiss() # Отклоняем алерт
#print(alert.text) # Вывод текста из алерта
