from selenium import webdriver
from selenium.webdriver.common.keys import Keys

Idno = []
Fis = []

PATH = "..//chromedriver"

driver = webdriver.Chrome(PATH)

driver.get("https://programari2.registru.md")


def initial():

    e = driver.find_element_by_name("serviceId").click()

    b = driver.find_element_by_xpath('//*[@id="serviceId"]/option[11]').click()

    c = driver.find_element_by_xpath('').click()

    c2 = driver.find_element_by_xpath('//*[@id="terms"]/p/input[2]').click()

    c3 = driver.find_element_by_xpath('//*[@id="terms"]/p/input[3]').click()

# e.click()
if __name__ == "__main__":
    initial()

# driver.quit()
