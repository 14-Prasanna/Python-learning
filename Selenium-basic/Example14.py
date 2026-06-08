from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
import time

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


def dismiss_vignette(driver):
    try:
        driver.execute_script("""
            var vignette = document.querySelector('div#google_vignette');
            if (vignette) vignette.remove();

            var overlays = document.querySelectorAll('div[id*="vignette"], div[id*="interstitial"]');
            overlays.forEach(function(el) { el.remove(); });

            var iframes = document.querySelectorAll('iframe');
            iframes.forEach(function(f) {
                var style = window.getComputedStyle(f);
                if (style.position === 'fixed' && parseInt(style.zIndex) > 1000) {
                    f.remove();
                }
            });
        """)
        print("Vignette ad dismissed")
    except Exception as e:
        print(f"Vignette dismissal skipped: {e}")


profile = FirefoxProfile()

options = Options()
options.add_argument("--width=1920")
options.add_argument("--height=1080")


driver = webdriver.Firefox(options=options)
driver.maximize_window()
wait = WebDriverWait(driver, 20)
action = ActionChains(driver)

driver.get("https://automationexercise.com/")
dismiss_ads(driver)
dismiss_vignette(driver)

print(driver.current_url)
print(driver.current_window_handle)


element = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/products']")))
dismiss_vignette(driver)
driver.execute_script("arguments[0].click();", element)

print(driver.current_url)


try:
    wait.until(EC.url_contains("/products"))
except:
    
    print("Navigation intercepted, going to /products directly...")
    driver.get("https://automationexercise.com/products")
    dismiss_ads(driver)
    dismiss_vignette(driver)

print(f"Current URL after navigation: {driver.current_url}")

wait.until(EC.presence_of_element_located((By.CLASS_NAME, "single-products")))

product_container = wait.until(
    EC.presence_of_element_located((By.XPATH,
        "//div[contains(@class,'product-image-wrapper')]//img[@src='/get_product_picture/1']/ancestor::div[contains(@class,'single-products')]"))
)

driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", product_container)
time.sleep(0.5)

dismiss_ads(driver)
dismiss_vignette(driver)


product_container = wait.until(
    EC.presence_of_element_located((By.XPATH,
        "//div[contains(@class,'product-image-wrapper')]//img[@src='/get_product_picture/1']/ancestor::div[contains(@class,'single-products')]"))
)

action.move_to_element(product_container).perform()
time.sleep(1)

overlay = wait.until(EC.visibility_of_element_located((By.XPATH,
    "//div[contains(@class,'product-overlay') and .//p[text()='Blue Top']]"
)))

getThepopup = overlay.value_of_css_property("display")

assert "block" in getThepopup, \
    "Failed: The hover is not present"

print("Hover verified: overlay is visible")

add_to_cart_btn = overlay.find_element(By.XPATH,
    ".//a[contains(normalize-space(text()),'Add to cart')]"
)

dismiss_vignette(driver)

action.move_to_element(add_to_cart_btn).click().perform()

wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class='modal-header']/child::h4")))

msg = driver.find_element(By.XPATH, "//div[@class='modal-header']/child::h4")

assert "Added" in msg.text, \
    "Failed: The product was not added to the cart"

print("The product is added to cart")
print("Add to Cart button clicked successfully!")

click_the_Add = driver.find_element(By.XPATH, "//div[@class = 'modal-footer']/child::button[text() = 'Continue Shopping']")
action.move_to_element(click_the_Add).click().perform()

action.move_to_element(driver.find_element(By.XPATH, "//ul[@class = 'nav navbar-nav']//a[@href = '/view_cart']")).click().perform()

cart_to_checkout = driver.find_element(By.XPATH, "//div[@class = 'row']/descendant::a[text() = 'Proceed To Checkout']")

wait.until(EC.visibility_of_element_located(cart_to_checkout)).click()

msgCheckout = driver.find_element(By.XPATH, "//p[text() = 'Register / Login account to proceed on checkout.']").text

assert "Register / Login account to proceed on checkout." in msgCheckout, \
"Failed: the product not added to the checkout"

print("The pop-up Cart to checkout")






//p[@class = 'text-center']/child::a[@href = '/login']
