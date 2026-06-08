import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options

# Optional: configure Firefox profile with ad blocking preferences
options = Options()
options.set_preference("dom.disable_open_during_load", True)
options.set_preference("privacy.trackingprotection.enabled", True)   # Firefox built-in tracker blocking
options.set_preference("privacy.trackingprotection.pbmode.enabled", True)

driver = webdriver.Firefox(options=options)

# ❌ Removed CDP calls — not supported in Firefox
# driver.execute_cdp_cmd(...)  <-- DELETE THESE LINES

driver.get("https://leafground.com/select.xhtml")
driver.maximize_window()

wait = WebDriverWait(driver, 10)

search = wait.until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "input[id='j_idt87:auto-complete_input']"))
)

search.send_keys("aws")
search.send_keys(Keys.ENTER)

time.sleep(0.5) 

search.send_keys("PostMan")
search.send_keys(Keys.ENTER)

time.sleep(2)

wait.until(
    EC.element_to_be_clickable((By.XPATH, "//label[@id='j_idt87:lang_label']"))
).click()

dropdown = wait.until(
    EC.presence_of_all_elements_located(
        (By.XPATH, "//ul[@id='j_idt87:lang_items']//li")
    )
)

for drop in dropdown:
    text = drop.text.strip()
    print("Option found:", text)

    if text == "English":
        drop.click()
        print("Selected:", text)
        break

driver.quit()