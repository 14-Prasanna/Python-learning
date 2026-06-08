from re import sub

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def dismiss_ads(driver):
    try:
        driver.execute_script("""
            document.querySelectorAll(
                "iframe, .adsbygoogle, [id*='google_ads'], [id*='aswift']"
            ).forEach(el => el.remove());
        """)
        print("Ads removed")
    except Exception as e:
        print("No ads found:", e)


d=webdriver.Chrome()
wait=WebDriverWait(d,10)
d.maximize_window()
d.get("https://automationexercise.com/")
dismiss_ads(d)
subcription=d.find_element(By.XPATH,"//h2[normalize-space()='Subscription']").text
print(subcription)
wait.until(expected_conditions.visibility_of_element_located((By.XPATH,"//input[@id='susbscribe_email']"))).send_keys("tamil@gmail.com")
d.find_element(By.XPATH,"//button[@id='subscribe']").click()
msg=d.find_element(By.XPATH,"//div[@class='alert-success alert']").text
print(msg)
assert msg=="You have been successfully subscribed!"