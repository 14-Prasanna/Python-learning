from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.common.exceptions import TimeoutException
from webdriver_manager.firefox import GeckoDriverManager


# ── Ad Dismissal Helper ───────────────────────────────────────────────────────
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


# ── Firefox Options ───────────────────────────────────────────────────────────
options = Options()
options.add_argument("--headless")
options.add_argument("--width=1920")
options.add_argument("--height=1080")
options.set_preference("network.proxy.type", 0)
options.set_preference("browser.cache.disk.enable", False)
options.set_preference("browser.cache.memory.enable", False)
options.set_preference("network.http.connection-timeout", 30)
options.set_preference("network.http.response.timeout", 30)

# ── Driver Setup ──────────────────────────────────────────────────────────────
service = Service(GeckoDriverManager().install())
driver  = webdriver.Firefox(service=service, options=options)
driver.set_page_load_timeout(30)

wait       = WebDriverWait(driver, 15)
fluid_wait = WebDriverWait(driver, timeout=10.0, poll_frequency=0.2, ignored_exceptions=[Exception])

print("Firefox is assigned")

# ── Test ──────────────────────────────────────────────────────────────────────
try:
    driver.get("https://automationexercise.com/")
    print("Home URL:", driver.current_url)

    driver.find_element(By.XPATH, "//a[@href='/login']").click()
    dismiss_ads(driver)
    print("Login page URL:", driver.current_url)

    wait.until(EC.visibility_of_element_located((
        By.XPATH, "//form[@action='/login']/child::input[@name='email']"
    )))

    # ── FIX 1: dismiss ads BEFORE interacting with the form ──────────────────
    dismiss_ads(driver)

    driver.find_element(
        By.XPATH, "//form[@action='/login']/child::input[@name='email']"
    ).send_keys("testlogin@gmail.com")   # ← replace with your registered email

    driver.find_element(
        By.XPATH, "//form[@action='/login']/child::input[@name='password']"
    ).send_keys("1234567890")            # ← replace with your correct password

    driver.find_element(
        By.XPATH, "//form[@action='/login']/child::button[text()='Login']"
    ).click()

    dismiss_ads(driver)

    # ── FIX 2: check for login failure BEFORE waiting for logged-in state ────
    # If credentials are wrong, the site shows an error paragraph — catch it early
    try:
        error_msg = WebDriverWait(driver, 3).until(EC.presence_of_element_located((
            By.XPATH, "//form[@action='/login']/p[contains(@style,'color: red') or text()='Your email or password is incorrect!']"
        )))
        raise AssertionError(
            f"[LOGIN FAILED] Site returned error: '{error_msg.text}'. "
            f"Check your email/password credentials."
        )
    except TimeoutException:
        pass  # No error message found — login likely succeeded, continue

    # ── FIX 3: wait for the navbar "Logged in as" text ───────────────────────
    try:
        userName = fluid_wait.until(EC.presence_of_element_located((
            By.XPATH, "//ul[@class='nav navbar-nav']//a[contains(., 'Logged in as')]"
        )))
    except TimeoutException:
        # Dump the page source snippet to help diagnose what actually rendered
        nav_html = driver.find_element(By.XPATH, "//ul[@class='nav navbar-nav']").get_attribute("innerHTML")
        raise AssertionError(
            f"[LOGIN FAILED] 'Logged in as' text not found in navbar after login.\n"
            f"Navbar HTML: {nav_html}\n"
            f"Current URL: {driver.current_url}"
        )

    checkuser = userName.text
    print("Navbar text:", checkuser)

    # NOTE: update 'Test cases' to your exact registered display name
    assert "Logged in as Test cases" in checkuser, \
        f"[ASSERT FAILED] Expected 'Logged in as Test cases' | Actual: '{checkuser}'"
    print("Login verified: username shown correctly")

    # ── Logout ────────────────────────────────────────────────────────────────
    url_before_logout = driver.current_url
    print("URL before logout:", url_before_logout)

    driver.find_element(
        By.XPATH,
        "//ul[@class='nav navbar-nav']/descendant::a[@href='/logout']"
    ).click()

    dismiss_ads(driver)

    wait.until(EC.url_changes(url_before_logout))
    url_after_logout = driver.current_url
    print("URL after logout:", url_after_logout)

    assert url_after_logout != url_before_logout, \
        f"[ASSERT FAILED] Logout did not happen — URL unchanged: '{url_after_logout}'"
    print("Logout successful: URL changed to", url_after_logout)

except Exception as e:
    print(f"Test failed with error: {e}")
    raise

finally:
    driver.quit()
    print("Browser closed")