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

url = "https://www.infobase.md/ro/search?page=1&q="
driver = webdriver.Firefox(executable_path="../geckodriver")


def enter_dno():

    driver.implicitly_wait(10)
    search_engine = driver.find_element(
        By.XPATH, '//*[@id="index"]/div/main/div/div[3]/div[1]/div/div/div/h2/a'
    ).click()
    return search_engine


def acces():

    try:
        for x in idno:
            y = driver.get(url + x)
            p = url + x
            print(p)
            enter_dno()
            # driver.implicitly_wait(10)

            parsing()

    finally:
        pass
        # print('Entered the page')
    return y


# --------------------------------------------------------


def parsing():

    # global soup
    html_code = driver.page_source
    markup = driver.page_source
    soup = BeautifulSoup(html_code, "lxml")

    # for x in soup :
    x = soup.select("title")
    y = soup.find_all(class_="MuiGrid-root MuiGrid-item MuiGrid-grid-md-12")

    print(x)
    print(y)


def reunion():

    try:
        acces()

    finally:
        pass
        print(
            "end of test--------------------------------------------------------------------------------"
        )


if __name__ == "__main__":

    try:
        reunion()

    except Exception as e:
        print(e)
    finally:
        # driver.implicitly_wait(20)
        driver.quit()
