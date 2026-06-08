import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
import time


@pytest.mark.parametrize("browser", ["firefox", "edge"])
@pytest.mark.parametrize("search_term", ["selenium", "pytest", "selenium locators"])
def test_google_search(browser, search_term):
    
    driver = None
    
    if browser == "firefox":
        options = FirefoxOptions()
        options.add_argument("--headless")
        driver = webdriver.Firefox(options=options)
        
    elif browser == "edge":
        options = EdgeOptions()
        options.add_argument("--headless")
        driver = webdriver.Edge(options=options)
    
    try:
        driver.maximize_window()
        driver.get("https://www.google.com")
        
        driver.find_element(By.NAME, "q").send_keys(search_term)
        time.sleep(2)
        
        driver.find_element(By.NAME, "btnK").click()
        time.sleep(5)
        
        print(f" Search completed for: '{search_term}' on {browser.upper()}")
        
    finally:
        if driver:
            driver.quit()