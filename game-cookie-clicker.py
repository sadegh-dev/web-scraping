
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

PATH = "/usr/bin/chromedriver"
driver = webdriver.Chrome(PATH)
driver.get("https://orteil.dashnet.org/cookieclicker/")

