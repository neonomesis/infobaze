from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

# import unittest
NoSuchElementException == True


driver = webdriver.Firefox(executable_path="../geckodriver")


driver.get("https://www.google.com/")

driver.find_element_by_class_name('ssss')

if NoSuchElementException:
    driver.quit()
