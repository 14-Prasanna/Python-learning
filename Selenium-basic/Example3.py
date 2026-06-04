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

wait.until(EC.visibility_of_element_located((By.XPATH, "//form[@action = '/login']/child::p[text() = 'Your email or password is incorrect!']")))

elements = driver.find_element(By.XPATH, "//form[@action = '/login']/child::p[text() = 'Your email or password is incorrect!']")

val = elements.text

print(val)

assert val == "Success: Your email or password is incorrect!", \
"Failed: The wrong email and password is accepted"

driver.quit()