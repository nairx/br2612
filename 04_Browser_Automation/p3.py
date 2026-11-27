from selenium import webdriver
from selenium.webdriver.common.by import By 
from time import sleep
driver = webdriver.Chrome()
# driver.get("https://reactapp-br.vercel.app")
# driver.get("https://www.broadridge.com")
driver.get("https://www.google.com")
# element = driver.find_element(By.TAG_NAME,"h1")
# print(element.text)
sleep(2)
link = driver.find_element(By.PARTIAL_LINK_TEXT,"About")
link.click()
sleep(3)
driver.quit()