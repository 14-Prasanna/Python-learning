import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver = webdriver.Firefox()
print("Firefox is assigned")

driver.maximize_window()

driver.get("https://automationexercise.com/")

print(driver.current_url)

signup = driver.find_element(By.XPATH, "//a[@href='/login']")
signup.click()

print(driver.current_url)

name = driver.find_element(By.NAME, "name")
name.send_keys("Shri_Deepak")

email = driver.find_element(By.XPATH, "//input[@data-qa = 'signup-email']")
email.send_keys("deepak18@gmail.com")

driver.find_element(By.XPATH, "//button[@data-qa='signup-button']").click()

time.sleep(10)

passwords = driver.find_element(By.XPATH, "//input[@id='password']")
passwords.send_keys("1234567890")

firstName = driver.find_element(By.XPATH, "//input[@id='first_name']")
firstName.send_keys("Prasanna")

lastName = driver.find_element(By.XPATH, "//input[@id='last_name']")
lastName.send_keys("Venkatesh")

address = driver.find_element(By.XPATH, "//input[@id='address1']")
address.send_keys("egsdrfghujio, egyfuijow")

country = Select(driver.find_element(By.XPATH, "//select[@id='country']"))
country.select_by_visible_text("India")

state = driver.find_element(By.XPATH, "//input[@id='state']")
state.send_keys("Tamilnadu")

city = driver.find_element(By.XPATH, "//input[@id='city']")
city.send_keys("Trichy")

zipcode = driver.find_element(By.XPATH, "//input[@id='zipcode']")
zipcode.send_keys("620006")

phone = driver.find_element(By.XPATH, "//input[@id='mobile_number']")
phone.send_keys("0987654321")

driver.find_element(By.XPATH, "//button[text()='Create Account']").click()

time.sleep(10)

success = driver.find_element(By.XPATH, "//h2[@data-qa='account-created']")

print(success.text)

val = success.text.lower()

if "account created!" in val:
    print("The registration is successful")
else:
    print("The registration is unsuccessful")


ContinueAc = driver.find_element(By.XPATH, "//a[text() = 'Continue']").click()
time.sleep(10)

userName = driver.find_element(By.XPATH, "//ul[@class = 'nav navbar-nav']/descendant::a[text() = ' Logged in as ']")
print(userName.text)
checkuser = userName.text

if "Logged in as Shri_Deepak" in checkuser:
    print("The Logged username is show")
else:
    print("The logged username is not show")

driver.find_element(By.XPATH, "//a[@href = '/delete_account']").click()

time.sleep(10)

deleteSuc = driver.find_element(By.XPATH, "//p[text() = 'Your account has been permanently deleted!']")

print(deleteSuc.text)

deleteMsg = deleteSuc.text

if "Your account has been permanently deleted!" in deleteMsg:
    print("The account deleted successfully")
else:
    print("The account is not deleted")


ContinueAc = driver.find_element(By.XPATH, "//a[text() = 'Continue']").click()
time.sleep(10)


driver.close()
