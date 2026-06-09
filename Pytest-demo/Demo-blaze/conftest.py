import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.support.ui import WebDriverWait
from resources.ConfigReader import get_value


@pytest.fixture()
def setup(request):

    url = get_value("Basic Info", "url")

    options = FirefoxOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")

    driver = webdriver.Firefox(options=options)
    driver.get(url)
    driver.maximize_window()

    wait = WebDriverWait(driver, 10)

    request.cls.driver = driver
    request.cls.wait   = wait

    yield

    driver.quit()
