import time
from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys


driver = webdriver.Firefox()

driver.maximize_window() 
driver.get("https://www.google.com/")
time.sleep(3)

print(driver.current_url)
print(driver.title)

elements = driver.find_element(By.NAME, "q")
if(elements.is_enabled):
    print("The button is enabled")
else:
    print("The button is not enabled")

elements.send_keys("Srh vs CSK")
elements.send_keys(Keys.ENTER)

time.sleep(30) 
print(driver.current_url)
driver.close()