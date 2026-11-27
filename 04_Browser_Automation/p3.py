from selenium import webdriver
from selenium.webdriver.common.by import By 

driver = webdriver.Chrome()

# driver.get("https://reactapp-br.vercel.app")

driver.get("https://www.broadridge.com")

element = driver.find_element(By.TAG_NAME,"h1")

print(element.text)

driver.quit()