from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


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


def scroll_to_element(driver, element):
    """
    Scrolls until the given WebElement is in view using ActionChains.
    Requires Selenium 4.2+ (uses scroll_to_element internally).
    """
    ActionChains(driver)\
        .scroll_to_element(element)\
        .perform()
    print(f"ActionChains: scrolled to element → <{element.tag_name}>")



def scroll_by_amount(driver, delta_x=0, delta_y=500):
    """
    Scrolls the page by the given pixel amount using ActionChains.
    delta_x → horizontal scroll (px)
    delta_y → vertical scroll (px)
    Origin is the top-left of the viewport (0, 0).
    """
    ActionChains(driver)\
        .scroll_by_amount(delta_x, delta_y)\
        .perform()
    print(f"ActionChains: scrolled by delta_x={delta_x}px, delta_y={delta_y}px")



d = webdriver.Firefox()
d.maximize_window()
wait = WebDriverWait(d, 10)

try:
    
    d.get("https://automationexercise.com")


    products = d.find_element(By.XPATH, "//a[@href='/products']")
    scroll_to_element(d, products)          
    products.click()

    
    dismiss_ads(d)

    
    scroll_by_amount(d, delta_y=400)      

    
    product_name_elements = d.find_elements(
        By.XPATH, "//img/following-sibling::p"
    )
    product_names = []
    for item in product_name_elements:
        product_names.append(item.text)

    if len(product_names) == 34:
        print(f"Product count verified: {len(product_names)} products found")
    else:
        print(f"Product count mismatch: found {len(product_names)} (expected 34)")

    
    first_product = d.find_element(
        By.XPATH,
        "//div[@class='col-sm-9 padding-right']//div[2]//div[1]//div[2]//ul[1]//li[1]//a[1]"
    )
    scroll_to_element(d, first_product)    
    first_product.click()

    
    title = wait.until(
        EC.visibility_of_element_located(
            (By.XPATH, "//h2[normalize-space()='Blue Top']")
        )
    ).text

    assert title == "Blue Top", f"Unexpected title: {title}"
    print(f"Product title verified: '{title}'")

except AssertionError as ae:
    print(f"Assertion Failed: {ae}")

except Exception as e:
    print(f"Test Error: {e}")

finally:
    d.quit()