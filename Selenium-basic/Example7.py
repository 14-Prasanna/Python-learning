from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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

d = webdriver.Chrome()
d.maximize_window()
wait=WebDriverWait(d,10)
d.get("https://automationexercise.com")
products=d.find_element(By.XPATH, "//a[@href='/products']")
products.click()
dismiss_ads(d)
list = d.find_elements(By.XPATH, "//img/following-sibling::p")
l=[]
for i in list:
    l.append(i.text)
if len(l)==34:
    print("Yes")
d.find_element(By.XPATH,"//div[@class='col-sm-9 padding-right']//div[2]//div[1]//div[2]//ul[1]//li[1]//a[1]").click()
title=wait.until(EC.visibility_of_element_located((By.XPATH,"//h2[normalize-space()='Blue Top']"))).text
assert title=="Blue Top"