from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


PATH = "/usr/bin/chromedriver"
driver = webdriver.Chrome(PATH)

driver.get("https://www.w3schools.com/")

link = driver.find_element(by=By.LINK_TEXT, value="Python Reference")
link.click()

try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Built-in Functions"))
    ) 
    element.click()

    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "format()"))
    ) 
    element.click()

    driver.back()
    driver.back()
    driver.back()
    driver.forward()
    driver.forward()
    driver.forward()

except:
    print('Error! , Element Not Load')

finally:
    driver.quit()

