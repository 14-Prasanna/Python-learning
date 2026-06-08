from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager

options = Options()
options.add_argument("--headless")

driver = webdriver.Firefox(
    executable_path=GeckoDriverManager().install(),
    options=options
)

driver.implicitly_wait(10)

driver.get("https://automationexercise.com")

driver.find_element(By.XPATH, "//a[normalize-space()='Signup / Login']").click()

driver.find_element(By.XPATH, "//input[@placeholder='Name']").send_keys("Tamil")

driver.find_element(
    By.XPATH,
    "//input[@data-qa='signup-email']"
).send_keys("tamilkumar0027@gmail.com")

driver.find_element(
    By.XPATH,
    "//button[normalize-space()='Signup']"
).click()

errorMessage = driver.find_element(
    By.XPATH,
    "//p[normalize-space()='Email Address already exist!']"
).text

print(errorMessage)

assert errorMessage == "Email Address already exist!"

driver.quit()   