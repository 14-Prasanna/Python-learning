import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService

@pytest.mark.parametrize("search_term", ["selenium", "pytest", "selenium locators"])
def test_google_search(search_term):
    driver = None
    try:
        
        service = FirefoxService(GeckoDriverManager().install())
        options = webdriver.FirefoxOptions()
        options.add_argument("--headless")           
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        
        driver = webdriver.Firefox(service=service, options=options)
        
        driver.get("https://www.google.com")
        
        
        search_box = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "q"))
        )
        search_box.send_keys(search_term)
        time.sleep(1)
        
        
        search_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.NAME, "btnK"))
        )
        search_button.click()
        
        time.sleep(3)  
        
        print(f"Search completed for: '{search_term}'")
        
    finally:
        if driver:
            driver.quit()  
