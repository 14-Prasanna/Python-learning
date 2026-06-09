import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

@pytest.fixture(params=["firefox", "edge"])
def setup(request):
    driver = None
    wait = None
    if request.param == "firefox":
        driver = webdriver.Firefox()
    elif request.param == "edge":
        driver = webdriver.Edge()

    driver.maximize_window()
    wait = WebDriverWait(driver, 10)
    driver.get("https://tutorialsninja.com/demo/index.php?route=common/home")
    request.cls.driver = driver
    yield driver
    driver.quit()

    