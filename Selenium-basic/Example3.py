import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager


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



options = Options()
options.add_argument("--headless")
options.add_argument("--width=1920")
options.add_argument("--height=1080")


options.set_preference("network.proxy.type", 0)


options.set_preference("browser.cache.disk.enable", False)
options.set_preference("browser.cache.memory.enable", False)


options.set_preference("network.http.connection-timeout", 30)
options.set_preference("network.http.response.timeout", 30)
service = Service(GeckoDriverManager().install())
driver = webdriver.Firefox(service=service, options=options)


driver.set_page_load_timeout(30)

wait = WebDriverWait(driver, 15)
print("Firefox is assigned")


try:
    driver.get("https://automationexercise.com/")
    print("Current URL:", driver.current_url)

    driver.find_element(By.XPATH, "//a[@href='/login']").click()
    dismiss_ads(driver)
    print("Navigated to login. Current URL:", driver.current_url)

    wait.until(EC.visibility_of_element_located((
        By.XPATH, "//form[@action='/login']/child::input[@name='email']"
    )))

    login_email = driver.find_element(
        By.XPATH, "//form[@action='/login']/child::input[@name='email']"
    )
    login_email.send_keys("testlogin@gmail.com")

    login_pass = driver.find_element(
        By.XPATH, "//form[@action='/login']/child::input[@name='password']"
    )
    login_pass.send_keys("wrongpassword")

    login_btn = driver.find_element(
        By.XPATH, "//form[@action='/login']/child::button[text()='Login']"
    )
    login_btn.click()

    dismiss_ads(driver)

    wait.until(EC.visibility_of_element_located((
        By.XPATH,
        "//form[@action='/login']/child::p[text()='Your email or password is incorrect!']"
    )))

    error_element = driver.find_element(
        By.XPATH,
        "//form[@action='/login']/child::p[text()='Your email or password is incorrect!']"
    )

    val = error_element.text
    print("Error message shown:", val)

    assert val == "Your email or password is incorrect!", \
        "Failed: The wrong credentials error message was not shown"

    print("Passed: Incorrect credentials are rejected as expected")

except Exception as e:
    print(f"Test failed with error: {e}")
    raise

finally:
    driver.quit()
    print("Browser closed")