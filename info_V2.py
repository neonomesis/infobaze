from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time


idno = ["10026000566", "1003602004112", "1009600017846", "1013606000397"]

url = "https://www.infobase.md/ro/search?page=1&q="
driver = webdriver.Firefox(executable_path="../geckodriver")

# enter the program, accesing web, looping it, writing it


def acces():

    try:
        for x in idno:
            y = driver.get(url + x)
            p = url + x
            print(p)
            enter_dno()
            time.sleep(1)
            parsing()
            importing()
    except:
        print('no element')
        pass
    finally:
        pass


# entering link of idno


def enter_dno():
    try:
        driver.implicitly_wait(10)
        search_engine = driver.find_element(
            By.XPATH, '//*[@id="index"]/div/main/div/div[3]/div[1]/div/div/div/h2/a'
        ).click()
    except:
        print('no element')
        pass
    finally:
        pass


# parsing web


def parsing():
    global soup
    global p, c, n, x

    html_code = driver.page_source
    soup = BeautifulSoup(html_code, "lxml")

    try:

        x = soup.select("title")
        c = soup.find(class_="MuiTypography-root MuiTypography-h2").get_text("\n")
        p = soup.select_one(".MuiTableBody-root").get_text("\n")  # .descendants
        n = soup.find(class_="MuiGrid-root MuiGrid-item MuiGrid-grid-md-4").get_text(
            "\n"
        )
    except:
        print('no element')
        pass
    finally:
        pass


# for clasification not working, not using


def pretyer():
    # parsing()
    dates = {"IDNO": "n"}


# creating file, writin it


def importing():
    try:
        with open("test.txt", "a") as f:

            for o in c:
                f.write(o)
            f.write("\n")
            for o in p:
                f.write(o)
            for o in n:
                f.write(o)

            f.write("\n")
            f.write("-----------------")
            f.write("\n")
            f.close()
    except:
        print('no element')
        pass
    finally:
        pass


# program start

if __name__ == "__main__":

    try:
        acces()

    except Exception as e:
        print(e)
    finally:
        driver.quit()
