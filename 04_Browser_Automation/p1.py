#pip install selenium 

from selenium import webdriver 

driver = webdriver.Chrome() 
# driver = webdriver.Edge() 

driver.get("https://www.broadridge.com")

print(driver.title)

driver.quit()