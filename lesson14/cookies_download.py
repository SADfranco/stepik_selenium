import os
import pickle
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 10, poll_frequency=1)


driver.get("http://users.bugred.ru/")

button = ("xpath", "//span[text()='Войти']")

wait.until(EC.element_to_be_clickable(button)).click()

login = ("xpath", '//input[@name="login"]')
password = ("xpath", '//input[@name="password"]')
button_login = ("xpath", '//input[@type="submit"]')

wait.until(EC.element_to_be_clickable(login)).send_keys("test@mail.com")
wait.until(EC.element_to_be_clickable(password)).send_keys("Zaqxsw1234")


wait.until(EC.element_to_be_clickable(button_login)).click()

cookies = driver.get_cookie("PHPSESSID")
pickle.dump(driver.get_cookie("PHPSESSID"), open(os.getcwd() + "/cookies/cookies.pkl", "wb"))
print(cookies)
