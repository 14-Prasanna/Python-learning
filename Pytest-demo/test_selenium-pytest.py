import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


@pytest.mark.parametrize("search_term", ["selenium", "pytest", "selenium locators"])
def test_google_search(search_term):
    driver = webdriver.Firefox()
    
    try:
        driver.get("https://www.google.com")          
        
        
        driver.find_element(By.NAME, "q").send_keys(search_term)
        time.sleep(3)
        
        
        driver.find_element(By.NAME, "btnK").click()   
        
        time.sleep(5)  
        
        print(f"✅ Search completed for: {search_term}")
        
    finally:
        driver.close()   