from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import ElementNotInteractableException
from bs4 import BeautifulSoup
import requests


idno = ["1002600056626", "1003602004112", "1009600017846", "1013606000397"]

soup = BeautifulSoup("html.parser", "lxml")
url = "https://www.infobase.md/ro/search?page=1&q="


def acces():

    for x in idno:
        pint = url + x
        print(pint)
    return pint


driver = webdriver.Firefox(executable_path="../geckodriver")

driver.implicitly_wait(5)


def enter_dno():
    driver.implicitly_wait(10)
    search_engine = driver.find_element(
        By.XPATH, '//*[@id="index"]/div/main/div/div[3]/div[1]/div/div/div/h2/a'
    ).click()


def parsing():
    for y in parsing():
        request = requests.get(url)
        print(request.status_code)


if __name__ == "__main__":
    try:
        for x in idno:
            # acces()
            driver.get(url + x)
            enter_dno()
            parsing()

    # except Exception as e:
    #     print(e)
    finally:
        driver.implicitly_wait(20)
        # driver.quit()
