from selenium import webdriver
from selenium.webdriver.common.by import By 
from time import sleep 
driver = webdriver.Chrome()
driver.get("https://browser-automation-lovat.vercel.app")
# driver.get("http://127.0.0.1:5500/index.html")
textbox = driver.find_element(By.NAME,"email")
textbox.send_keys("admin")
password = driver.find_element(By.NAME,"password")
password.send_keys("12344545T")
submit = driver.find_element(By.ID,"idSubmit")
submit.click()
element = driver.find_element(By.ID,"idMessage")
print(element.text)
driver.quit()