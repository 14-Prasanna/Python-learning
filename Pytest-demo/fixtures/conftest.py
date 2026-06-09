import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.support.ui import WebDriverWait


@pytest.fixture(params=["firefox", "edge"])
def setup(request):
    driver = None

    if request.param == "firefox":
        firefox_options = FirefoxOptions()
        firefox_options.add_argument("--headless")
        firefox_options.add_argument("--no-sandbox")
        firefox_options.add_argument("--disable-dev-shm-usage")
        firefox_options.add_argument("--window-size=1920,1080")
        driver = webdriver.Firefox(options=firefox_options)

    elif request.param == "edge":
        edge_options = EdgeOptions()
        edge_options.add_argument("--headless")
        edge_options.add_argument("--no-sandbox")
        edge_options.add_argument("--disable-dev-shm-usage")
        edge_options.add_argument("--window-size=1920,1080")
        edge_options.add_argument("--disable-gpu")
        driver = webdriver.Edge(options=edge_options)

    driver.maximize_window()
    wait = WebDriverWait(driver, 10)
    driver.get("https://tutorialsninja.com/demo/index.php?route=common/home")

    request.cls.driver = driver
    request.cls.wait = wait

    yield driver

    driver.quit()