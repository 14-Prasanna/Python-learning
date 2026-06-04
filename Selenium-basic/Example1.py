import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager


SCREENSHOT_DIR = "screenshots"
os.makedirs(SCREENSHOT_DIR, exist_ok=True)

def take_screenshot(driver, name):
    path = os.path.join(SCREENSHOT_DIR, f"{name}.png")
    driver.save_screenshot(path)
    print(f"Screenshot saved: {path}")


soft_assertions = []

options = Options()
options.add_argument("--headless")
options.add_argument("--width=1920")
options.add_argument("--height=1080")

driver = webdriver.Firefox(
    service=Service(GeckoDriverManager().install()),
    options=options
)

print("Firefox is assigned")
driver.maximize_window()

driver.get("https://automationexercise.com/")
print(driver.current_url)
take_screenshot(driver, "01_home_page")


signup = driver.find_element(By.XPATH, "//a[@href='/login']")
signup.click()
print(driver.current_url)
take_screenshot(driver, "02_login_page")


name = driver.find_element(By.NAME, "name")
name.send_keys("Shri_Deepak")

email = driver.find_element(By.XPATH, "//input[@data-qa = 'signup-email']")
email.send_keys("deepak18@gmail.com")

driver.find_element(By.XPATH, "//button[@data-qa='signup-button']").click()
time.sleep(10)
take_screenshot(driver, "03_account_info_page")


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
take_screenshot(driver, "04_after_create_account")


success = driver.find_element(By.XPATH, "//h2[@data-qa='account-created']")
print(success.text)

val = success.text.lower()


assert "account created!" in val, \
    f"[HARD ASSERT FAILED] Expected 'account created!' | Actual: '{val}'"

if "account created!" in val:
    print("The registration is successful")
else:
    print("The registration is unsuccessful")

take_screenshot(driver, "05_account_created")


driver.find_element(By.XPATH, "//a[text() = 'Continue']").click()
time.sleep(10)


userName = driver.find_element(
    By.XPATH,
    "//ul[@class = 'nav navbar-nav']/descendant::a[contains(text(),'Logged in as')]"
)
print(userName.text)
checkuser = userName.text


if "Logged in as Shri_Deepak" not in checkuser:
    msg = f"[SOFT ASSERT FAILED] Expected 'Logged in as Shri_Deepak' | Actual: '{checkuser}'"
    soft_assertions.append(msg)
    take_screenshot(driver, "FAIL_username_mismatch")
    print(msg)

if "Logged in as Shri_Deepak" in checkuser:
    print("The Logged username is show")
else:
    print("The logged username is not show")

take_screenshot(driver, "06_home_after_register")


driver.find_element(By.XPATH, "//a[@href = '/delete_account']").click()
time.sleep(10)
take_screenshot(driver, "07_after_delete_account")


deleteSuc = driver.find_element(
    By.XPATH,
    "//p[text() = 'Your account has been permanently deleted!']"
)
print(deleteSuc.text)
deleteMsg = deleteSuc.text


if "Your account has been permanently deleted!" not in deleteMsg:
    msg = f"[SOFT ASSERT FAILED] Expected 'Your account has been permanently deleted!' | Actual: '{deleteMsg}'"
    soft_assertions.append(msg)
    take_screenshot(driver, "FAIL_delete_message_mismatch")
    print(msg)

if "Your account has been permanently deleted!" in deleteMsg:
    print("The account deleted successfully")
else:
    print("The account is not deleted")

take_screenshot(driver, "08_account_deleted")


driver.find_element(By.XPATH, "//a[text() = 'Continue']").click()
time.sleep(10)
take_screenshot(driver, "09_final_home_page")

driver.close()
