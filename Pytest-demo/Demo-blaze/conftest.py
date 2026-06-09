import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.support.ui import WebDriverWait
from resources.ConfigReader import get_value


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="firefox",
        help="Browser to run tests: firefox or edge"
    )


@pytest.fixture()
def setup(request):

    url     = get_value("Basic Info", "url")
    browser = request.config.getoption("--browser")

    if browser.lower() == "firefox":
        options = FirefoxOptions()
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--window-size=1920,1080")
        driver = webdriver.Firefox(options=options)

    elif browser.lower() == "edge":
        options = EdgeOptions()
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-gpu")
        options.add_argument("--window-size=1920,1080")
        driver = webdriver.Edge(options=options)

    else:
        raise Exception(f"Unsupported browser: {browser}")

    driver.get(url)
    driver.maximize_window()

    wait = WebDriverWait(driver, 10)

    request.cls.driver = driver
    request.cls.wait   = wait

    yield

    driver.quit()
