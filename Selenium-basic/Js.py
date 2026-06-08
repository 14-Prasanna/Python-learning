from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

driver = webdriver.Firefox()
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/")


print(driver.execute_script("return document.title;"))


print(driver.execute_script("return {width: window.innerWidth, height: window.innerHeight};"))


name_field = driver.find_element(By.CSS_SELECTOR, "input#name.form-control")
driver.execute_script("arguments[0].value = 'Prasanna';", name_field)


email_field = driver.find_element(By.CSS_SELECTOR, "input#email.form-control")
driver.execute_script("arguments[0].remove();", email_field)


select_element = driver.find_element(By.CSS_SELECTOR, "select#country.form-control")


driver.execute_script("arguments[0].scrollIntoView();", select_element)  


Select_Drop = Select(select_element)
Select_Drop.select_by_visible_text("India")  

time.sleep(5)
driver.quit()