from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from bs4.formatter import HTMLFormatter
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
            # time.sleep(2)
            importing()

            print(
                "end of idno--------------------------------------------------------------------------------"
            )

    finally:
        pass


def enter_dno():

    driver.implicitly_wait(10)
    search_engine = driver.find_element(
        By.XPATH, '//*[@id="index"]/div/main/div/div[3]/div[1]/div/div/div/h2/a'
    ).click()


# --------------------------------------------------------


def parsing():
    global soup
    global p, c, n, x

    html_code = driver.page_source
    # markup = driver.page_source
    soup = BeautifulSoup(html_code, "lxml")

    try:

        x = soup.select("title")
        c = soup.find(class_="MuiTypography-root MuiTypography-h2").get_text('\n')
        p = soup.select_one(".MuiTableBody-root").get_text('\n')  # .descendants
        n = soup.find(class_="MuiGrid-root MuiGrid-item MuiGrid-grid-md-4").get_text('\n')

    finally:
        pass


def pretyer():
    # parsing()
    dates = {"IDNO": "n"}


def importing():
    with open("test.txt", "a") as f:
        
        for o in c:
            f.write(o)
        f.write('\n')
        for o in p:
            f.write(o)
        for o in n:
            f.write(o)
        
        f.write('\n')
        f.write('-----------------')  
        f.write('\n')     
        f.close()


def reunion():

    try:
        acces()
        # importing()
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
