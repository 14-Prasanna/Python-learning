from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


def dismiss_ads(driver):
    try:
        driver.execute_script("""
            document.querySelectorAll(
                "iframe, .adsbygoogle, [id*='google_ads'], [id*='aswift']"
            ).forEach(el => el.remove());
        """)
        print("Ads removed")
    except Exception as e:
        print("No ads found or error removing ads:", e)


def get_driver(browser="chrome"):
    if browser.lower() == "firefox":
        options = FirefoxOptions()
        options.add_argument("--headless")
        options.add_argument("--width=1920")
        options.add_argument("--height=1080")
        service = FirefoxService(GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service, options=options)
    else:
        options = ChromeOptions()
        options.add_argument("--headless")
        options.add_argument("--window-size=1920,1080")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-gpu")
        options.add_argument("--disable-extensions")
        options.add_argument("--disable-popup-blocking")
        service = ChromeService(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)
    
    driver.set_page_load_timeout(30)
    return driver


# Main Test
get_driver("firefox")
wait = WebDriverWait(driver, 15)

try:
    print("Navigating to https://automationexercise.com/")
    driver.get("https://automationexercise.com/")
    dismiss_ads(driver)

    subscription_heading = wait.until(
        EC.visibility_of_element_located((By.XPATH, "//h2[normalize-space()='Subscription']"))
    )
    print("Subscription heading found:", subscription_heading.text)

    email_field = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//input[@id='susbscribe_email']"))
    )
    email_field.clear()
    email_field.send_keys("prasanna@gmail.com")
    print("Email entered")

    driver.find_element(By.XPATH, "//button[@id='subscribe']").click()
    print("Subscribe button clicked")

    success_msg = wait.until(
        EC.visibility_of_element_located((By.XPATH, "//div[contains(@class,'alert-success')]"))
    ).text.strip()

    print("Success message:", success_msg)
    assert "successfully subscribed" in success_msg.lower()

    print("Test Passed: Subscription successful!")

except AssertionError as ae:
    print("Assertion Failed:", ae)
    raise
except Exception as e:
    print("Test Error:", e)
    raise
finally:
    driver.quit()
    print("Browser closed")