import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.support.ui import WebDriverWait


@pytest.fixture()
def setup():
    options = FirefoxOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")

    driver = webdriver.Firefox(options=options)
    driver.maximize_window()
    driver.get("https://demoblaze.com/")
    wait = WebDriverWait(driver, 10)

    yield driver, wait

    driver.quit()