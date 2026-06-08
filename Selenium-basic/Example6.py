import time

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

d = webdriver.Chrome()
d.maximize_window()
wait = WebDriverWait(
    d, 10, poll_frequency=2, ignored_exceptions=[NoSuchElementException]
)
d.get("https://automationexercise.com/")
d.find_element(By.XPATH, "//a[normalize-space()='Contact us']").click()
wait.until(
    EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Name']"))
).send_keys("Tamil")
d.find_element(By.XPATH, "//input[@placeholder='Email']").send_keys("tamil@gmail.com")
d.find_element(By.XPATH, "//input[@placeholder='Subject']").send_keys(
    "Related to not working website"
)
d.find_element(By.XPATH, "//textarea[@id='message']").send_keys(
    "Related to not working of the website"
)
d.find_element(By.XPATH, "//input[@name='upload_file']").send_keys(
    "C:\\Users\\tamil\\Downloads\\26.OOPs .pdf"
)
d.find_element(By.XPATH, "//input[@name='submit']").click()
alert = wait.until(EC.alert_is_present())
alert.accept()
msg = wait.until(
    EC.visibility_of_element_located(
        (By.XPATH, "//div[@class='status alert alert-success']")
    )
).text

print(msg)
assert msg == "Success! Your details have been submitted successfully."