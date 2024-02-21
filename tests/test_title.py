import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


def test_get_title():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--user-agent=Automation QA (Windows NT 6.1; rv:106.0) Gecko/20100101 Firefox/106.0")
    service = Service(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    driver.get("https://ya.ru/")
    title = driver.title
    url = driver.current_url
    print(f"Текущий заголовок страницы: {title}")
    print(f"Текущий url страницы: {url}")


    assert title == "Яндекс", "Заголовок не верный"
    assert url == "https://ya.ru/", "Верный url"

def test_get_url():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--user-agent=Automation QA (Windows NT 6.1; rv:106.0) Gecko/20100101 Firefox/106.0")
    service = Service(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    driver.get("https://ya.ru/")
    url = driver.current_url
    print(f"Текущий url страницы: {url}")

    assert url == "https://ya.ru/", "Верный url"




