from selenium import webdriver
from selenium.webdriver.common.by import By 

driver = webdriver.Chrome() 
# driver.get("https://browser-automation-lovat.vercel.app/index2.html")
driver.get("https://www.broadridge.com")

heading = driver.find_element(By.TAG_NAME,"h1")
paragraph = driver.find_elements(By.TAG_NAME,"p")

print("Heading",heading.text)
for p in paragraph:
    print(p.text)

driver.quit()