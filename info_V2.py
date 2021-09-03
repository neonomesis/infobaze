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
import time


idno = ["1002600056626", "1003602004112", "1009600017846", "1013606000397"]

url = "https://www.infobase.md/ro/search?page=1&q="
driver = webdriver.Firefox(executable_path="../geckodriver")

def acces():

    try:
        for x in idno:
            y = driver.get(url + x)
            p = url + x
            print(p)
            enter_dno()
            time.sleep(1)
            parsing()
            

    finally:
        pass


def enter_dno():

    driver.implicitly_wait(10)
    search_engine = driver.find_element(
        By.XPATH, '//*[@id="index"]/div/main/div/div[3]/div[1]/div/div/div/h2/a'
    ).click()


# --------------------------------------------------------


def parsing():

    html_code = driver.page_source
    markup = driver.page_source
    soup = BeautifulSoup(html_code, "lxml")
    try:
        
        # for x in soup :
        x = soup.select("title")
        c = soup.find(class_="MuiTypography-root MuiTypography-h2")

        
        print(x)
        print(c)

    finally:
        pass





# not working
def importing():
    f = open ('demon.txt', "w")
    y = f.write(parsing())
    # s = json.dumps()
    f.write(y)
    f.close()
    
    


def reunion():

    try:
        acces()
        
        # parsing()

    finally:
        pass
        print(
            "end of test--------------------------------------------------------------------------------"
        )


if __name__ == "__main__":

    try:
        reunion()
        # importing()

    except Exception as e:
        print(e)
    finally:
        # driver.implicitly_wait(20)
        driver.quit()
