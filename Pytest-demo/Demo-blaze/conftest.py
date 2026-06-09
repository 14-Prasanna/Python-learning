import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from resources.ConfigReader import get_value


@pytest.fixture()
def setup(request):

    url = get_value("Basic Info", "url")
    browser = get_value("Basic Info", "browser")

    if browser.lower() == "firefox":
        driver = webdriver.Firefox()
    else:
        raise Exception("Invalid browser")

    driver.get(url)
    driver.maximize_window()

    wait = WebDriverWait(driver, 10)

    request.cls.driver = driver
    request.cls.wait = wait

    yield

    driver.quit()