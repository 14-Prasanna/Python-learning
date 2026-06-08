import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture()
def setup(request):
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get("https://tutorialsninja.com/demo/index.php?route=common/home")
    request.cls.driver = driver
    yield driver
    driver.quit()