from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

#time.sleep(15)

PATH = "/usr/bin/chromedriver"

driver = webdriver.Chrome(PATH)

driver.get("http://www.tsetmc.com/Loader.aspx?ParTree=151311&i=67675656072510693")


