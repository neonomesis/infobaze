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


idno = "1007600023834"

soup = BeautifulSoup("html.parser", "lxml")
url = "https://www.infobase.md/ro/search"
driver = webdriver.Firefox(executable_path="../geckodriver")
driver.get(url)

driver.implicitly_wait(5)


def enter_dno():
    # search_engine = driver.find_element(
    #     By.XPATH, '//*[@id="index"]/div/main/div/div[1]/div/div'
    # ).click()
    search_engine = driver.find_element(
        By.XPATH, '//*[@id="index"]/div/main/div/div[1]'
    ).send_keys('333')
    # search_engine.clear()
    
    # search_engine.send_keys('333')
    

    driver.implicitly_wait(10)

    # search_engine.send_keys("idno")

    element = (
        WebDriverWait(driver, 10)
        .until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="index"]/div/main/div/div[3]/div[1]/div/div/div/h2')
            )
        )
        .click()
    )


# def parser():
# soup.

if __name__ == "__main__":
    try:
        enter_dno()
    # except Exception as e:
    #     print(e)
    finally:
        driver.implicitly_wait(20)
        driver.quit()
