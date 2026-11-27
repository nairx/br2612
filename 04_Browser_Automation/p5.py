from selenium import webdriver

driver = webdriver.Chrome() 

driver.get("https://www.broadridge.com")

driver.save_screenshot("website.png")