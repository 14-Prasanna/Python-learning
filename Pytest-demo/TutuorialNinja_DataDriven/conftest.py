import pytest
import os
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from resources.read_config import get_config


@pytest.fixture(scope="class")
def setup_and_teardown(request):
    browser = get_config("basic info", "browser").strip().lower()
    headless = os.getenv("HEADLESS", "true").lower() == "true"   # Default: True for CI

    if browser == "chrome":
        options = webdriver.ChromeOptions()
        if headless:
            options.add_argument("--headless")
            options.add_argument("--disable-gpu")
            options.add_argument("--window-size=1920,1080")
        driver = webdriver.Chrome(options=options)
        
    elif browser == "firefox":
        options = webdriver.FirefoxOptions()
        if headless:
            options.add_argument("--headless")
            options.add_argument("--width=1920")
            options.add_argument("--height=1080")
        driver = webdriver.Firefox(options=options)
        
    else:
        # Default to Firefox with headless
        options = webdriver.FirefoxOptions()
        options.add_argument("--headless")
        options.add_argument("--width=1920")
        options.add_argument("--height=1080")
        driver = webdriver.Firefox(options=options)

    driver.get(get_config("basic info", "url"))
    driver.maximize_window()
    
    request.cls.driver = driver
    request.cls.wait = WebDriverWait(driver, 15)   # Increased timeout slightly
    
    yield
    driver.quit()
