import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from resources.read_config import get_config


@pytest.fixture(scope="class")
def setup_and_teardown(request):
    browser = get_config("basic info", "browser").lower()
    
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    else:
        driver = webdriver.Firefox()  # default

    driver.get(get_config("basic info", "url"))
    driver.maximize_window()
    
    request.cls.driver = driver
    request.cls.wait = WebDriverWait(driver, 10)
    
    yield
    driver.quit()