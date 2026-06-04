import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

# ── Screenshot folder ──────────────────────────────────────────────
SCREENSHOT_DIR = "screenshots"
os.makedirs(SCREENSHOT_DIR, exist_ok=True)

def take_screenshot(driver, name):
    path = os.path.join(SCREENSHOT_DIR, f"{name}.png")
    driver.save_screenshot(path)
    print(f"Screenshot saved: {path}")

# ── Ad Dismissal Helper ────────────────────────────────────────────
def dismiss_ads(driver):
    try:
        driver.execute_script("""
            var iframes = document.querySelectorAll('iframe');
            for (var i = 0; i < iframes.length; i++) {
                var src = iframes[i].src || '';
                var id  = iframes[i].id  || '';
                if (
                    src.includes('doubleclick') ||
                    src.includes('googleads')   ||
                    src.includes('googlesyndication') ||
                    id.includes('aswift')       ||
                    id.includes('google_ads')
                ) {
                    iframes[i].remove();
                }
            }
        """)
        print("Ads dismissed")
    except Exception as e:
        print(f"Ad dismissal skipped: {e}")

# ── Safe Click Helper ──────────────────────────────────────────────
def safe_click(driver, xpath):
    dismiss_ads(driver)
    try:
        element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, xpath))
        )
        element.click()
    except Exception:
        print(f"Normal click failed, using JS click for: {xpath}")
        element = driver.find_element(By.XPATH, xpath)
        driver.execute_script("arguments[0].click();", element)

# ── Driver Setup ───────────────────────────────────────────────────
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

# ── Navigate to site ───────────────────────────────────────────────
driver.get("https://automationexercise.com/")
print(driver.current_url)
take_screenshot(driver, "01_home_page")

# ── Click Signup/Login ─────────────────────────────────────────────
safe_click(driver, "//a[@href='/login']")
print(driver.current_url)
take_screenshot(driver, "02_login_page")

# ── Fill Signup Form ───────────────────────────────────────────────
name = driver.find_element(By.NAME, "name")
name.send_keys("Shri_Deepak")

email = driver.find_element(By.XPATH, "//input[@data-qa = 'signup-email']")
email.send_keys("deepak18@gmail.com")

safe_click(driver, "//button[@data-qa='signup-button']")
time.sleep(10)
take_screenshot(driver, "03_account_info_page")

# ── Fill Account Details ───────────────────────────────────────────
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

safe_click(driver, "//button[text()='Create Account']")
time.sleep(10)
take_screenshot(driver, "04_after_create_account")

# ── HARD ASSERT — Account Created ─────────────────────────────────
success = driver.find_element(By.XPATH, "//h2[@data-qa='account-created']")
print(success.text)

val = success.text.lower()

# Hard Assert
assert "account created!" in val, \
    f"[HARD ASSERT FAILED] Expected 'account created!' | Actual: '{val}'"

if "account created!" in val:
    print("The registration is successful")
else:
    print("The registration is unsuccessful")

take_screenshot(driver, "05_account_created")

# ── Continue after Account Creation ───────────────────────────────
safe_click(driver, "//a[text() = 'Continue']")

# Wait for navbar to load after redirect
WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH, "//ul[@class='nav navbar-nav']"))
)
time.sleep(3)
take_screenshot(driver, "06_after_continue")

# ── SOFT ASSERT — Logged in as Shri_Deepak ────────────────────────
try:
    userName = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((
            By.XPATH,
            "//ul[@class='nav navbar-nav']//a[contains(., 'Logged in as')]"
        ))
    )
    print(userName.text)
    checkuser = userName.text

    # Soft Assert
    if "Logged in as Shri_Deepak" not in checkuser:
        msg = f"[SOFT ASSERT FAILED] Expected 'Logged in as Shri_Deepak' | Actual: '{checkuser}'"
        soft_assertions.append(msg)
        take_screenshot(driver, "FAIL_username_mismatch")
        print(msg)

    if "Logged in as Shri_Deepak" in checkuser:
        print("The Logged username is show")
    else:
        print("The logged username is not show")

except Exception as e:
    # Debug: print actual navbar HTML to console
    navbar_html = driver.execute_script("""
        var nav = document.querySelector('ul.nav.navbar-nav');
        return nav ? nav.innerHTML : 'Navbar not found';
    """)
    print(f"Navbar HTML: {navbar_html}")
    take_screenshot(driver, "FAIL_navbar_debug")
    msg = f"[SOFT ASSERT FAILED] 'Logged in as Shri_Deepak' element not found. Error: {e}"
    soft_assertions.append(msg)
    print(msg)

take_screenshot(driver, "07_home_after_register")

# ── Delete Account ─────────────────────────────────────────────────
safe_click(driver, "//a[@href = '/delete_account']")
time.sleep(10)
take_screenshot(driver, "08_after_delete_account")

# ── SOFT ASSERT — Account Deleted ─────────────────────────────────
deleteSuc = driver.find_element(
    By.XPATH,
    "//p[text() = 'Your account has been permanently deleted!']"
)
print(deleteSuc.text)
deleteMsg = deleteSuc.text

# Soft Assert
if "Your account has been permanently deleted!" not in deleteMsg:
    msg = f"[SOFT ASSERT FAILED] Expected 'Your account has been permanently deleted!' | Actual: '{deleteMsg}'"
    soft_assertions.append(msg)
    take_screenshot(driver, "FAIL_delete_message_mismatch")
    print(msg)

if "Your account has been permanently deleted!" in deleteMsg:
    print("The account deleted successfully")
else:
    print("The account is not deleted")

take_screenshot(driver, "09_account_deleted")

# ── Continue after Delete ──────────────────────────────────────────
safe_click(driver, "//a[text() = 'Continue']")
time.sleep(10)
take_screenshot(driver, "10_final_home_page")

driver.close()
