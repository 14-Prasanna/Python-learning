from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def dismiss_ads(driver):
    try:
        driver.execute_script("""
            var iframes = document.querySelectorAll('iframe');
            for (var i = 0; i < iframes.length; i++) {
                var src = iframes[i].src || '';
                var id  = iframes[i].id  || '';
                if (
                    src.includes('doubleclick')       ||
                    src.includes('googleads')         ||
                    src.includes('googlesyndication') ||
                    id.includes('aswift')             ||
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
driver.maximize_window()
wait = WebDriverWait(driver, 10)

try:
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")
    dismiss_ads(driver)

    driver.find_element(
        By.XPATH, "//*[@id='content']/div/ul/li[1]/button"
    ).click()

    simple_alert = wait.until(EC.alert_is_present())
    print(f"Simple Alert text : {simple_alert.text}")
    simple_alert.accept()                       
    result = driver.find_element(By.ID, "result").text
    print(f"Simple Alert result : {result}")
    assert result == "You successfully clicked an alert"

    
    driver.find_element(
        By.XPATH, "//*[@id='content']/div/ul/li[2]/button"
    ).click()

    confirm_alert = wait.until(EC.alert_is_present())
    print(f"Confirm Alert text : {confirm_alert.text}")
    confirm_alert.accept()                        
    result = driver.find_element(By.ID, "result").text
    print(f"Confirm Alert result : {result}")
    assert result == "You clicked: Ok"

    
    driver.find_element(
        By.XPATH, "//*[@id='content']/div/ul/li[3]/button"
    ).click()

    prompt_alert = wait.until(EC.alert_is_present())
    print(f"Prompt Alert text : {prompt_alert.text}")
    prompt_alert.send_keys("Prasanna")            
    prompt_alert.accept()
    result = driver.find_element(By.ID, "result").text
    print(f"Prompt Alert result : {result}")
    assert result == "You entered: Prasanna"

    print("All alert tests passed")

except AssertionError as ae:
    print(f"Assertion failed: {ae}")

except Exception as e:
    print(f"Test error: {e}")

finally:
    driver.quit()