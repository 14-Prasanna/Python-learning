import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait



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





driver = webdriver.Firefox()
wait = WebDriverWait(driver, 15)
print("Firefox is assigned")

driver.maximize_window()
driver.get("https://automationexercise.com/")
print(driver.current_url)

driver.find_element(By.XPATH, "//a[@href='/login']").click()
dismiss_ads(driver)
print(driver.current_url)


wait.until(EC.visibility_of_element_located((
    By.XPATH, "//form[@action = '/login']/child::input[@name = 'email']"
)))

login_email = driver.find_element(
    By.XPATH, "//form[@action = '/login']/child::input[@name = 'email']"
)
login_email.send_keys("testlogin@gmail.com")

login_pass = driver.find_element(
    By.XPATH, "//form[@action = '/login']/child::input[@name = 'password']"
)
login_pass.send_keys("1234567890")

login_btn = driver.find_element(
    By.XPATH, "//form[@action = '/login']/child::button[text() = 'Login']"
)
login_btn.click()

dismiss_ads(driver)

userName = wait.until(EC.presence_of_element_located((
    By.XPATH, "//ul[@class='nav navbar-nav']//a[contains(., 'Logged in as')]"
)))

print(userName.text)
checkuser = userName.text


assert "Logged in as Test cases" in checkuser, \
    f"[ASSERT FAILED] Expected 'Logged in as Test cases' | Actual: '{checkuser}'"
print("The Logged username is shown")

driver.find_element(By.XPATH, "//a[@href = '/delete_account']").click()

dismiss_ads(driver)

wait.until(EC.visibility_of_element_located((
    By.XPATH, "//p[text() = 'Your account has been permanently deleted!']"
)))

deleteSuc = driver.find_element(
    By.XPATH, "//p[text() = 'Your account has been permanently deleted!']"
)
print(deleteSuc.text)
deleteMsg = deleteSuc.text

assert deleteMsg == "Your account has been permanently deleted!", \
    "Failed: the account was not deleted"
print("The account deleted successfully")

driver.find_element(By.XPATH, "//a[text() = 'Continue']").click()

dismiss_ads(driver)

driver.quit()