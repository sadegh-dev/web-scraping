from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


PATH = "/usr/bin/chromedriver"
driver = webdriver.Chrome(PATH)

driver.get("http://boursepress.ir/")
#print(driver.title)


# Search

search = driver.find_element(by=By.NAME, value="q")
search.clear()
search.send_keys("پالایش یکم")
search.send_keys(Keys.RETURN)


try:
    content = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID,"ucSearch_divContent"))
    ) 

    # Read titles

    articles = content.find_elements(by=By.TAG_NAME, value="li")
    for article in articles :
        header = article.find_element(by=By.TAG_NAME, value= "a")
        print(header.text)

except:
    print('Error! , Element Not Load')

finally:
    driver.quit()

