import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture()
def setup():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get("https://demoblaze.com/")
    wait = WebDriverWait(driver, 10)

    yield driver, wait

    driver.quit()