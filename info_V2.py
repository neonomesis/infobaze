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



idno = ['1002600056626','1003602004112','1002600056626']

# def idn():
#     for x in idno:
    

soup = BeautifulSoup("html.parser", "lxml")
def acces():
    for x in idno:
        url = ("https://www.infobase.md/ro/search?page=1&q=" + x)
    else:
        print('finish')
        print(idno)
    return url

driver = webdriver.Firefox(executable_path="../geckodriver")
driver.get(acces())


driver.implicitly_wait(5)

def enter_dno():
    driver.implicitly_wait(10)
    search_engine = driver.find_element(
        By.XPATH, '//*[@id="index"]/div/main/div/div[3]/div[1]/div/div/div/h2/a'
    ).click()
   
def parsing():
    pass


if __name__ == "__main__":
    try:
        enter_dno()
    except Exception as e:
        print(e)
    finally:
        driver.implicitly_wait(20)
        # driver.quit()
