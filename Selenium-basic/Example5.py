from selenium import webdriver
from selenium.webdriver.common.by import By

d = webdriver.Chrome()
d.maximize_window()
d.implicitly_wait(10)
d.get("http://automationexercise.com")
d.find_element(By.XPATH, "//a[normalize-space()='Signup / Login']").click()
d.find_element(By.XPATH, "//input[@placeholder='Name']").send_keys("Tamil")
d.find_element(By.XPATH, "//input[@data-qa='signup-email']").send_keys(
    "tamilkumar0027@gmail.com"
)
d.find_element(By.XPATH, "//button[normalize-space()='Signup']").click()
errorMessage = d.find_element(
    By.XPATH, "//p[normalize-space()='Email Address already exist!']"
).text
print(errorMessage)
assert errorMessage == "Email Address already exist!"