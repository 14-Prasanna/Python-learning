import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver: webdriver.Firefox = None      


@pytest.fixture(autouse=True)
def setup():
    global driver
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get("https://tutorialninja.com/demo/")
    yield
    driver.quit()


def test_home_page():
    print("Current URL :", driver.current_url)
    print("Page Title  :", driver.title)

    assert "tutorialninja" in driver.current_url.lower()
    assert driver.title != ""
    print("Home page test passed!")


def test_search_product():
    search = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "input.form-control.input-lg"))
    )
    search.clear()
    search.send_keys("HP")
    search.send_keys(Keys.ENTER)

    search_result = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[@id='content']/h1"))
    )

    assert "Search - HP" in search_result.text
    print("Search bar test passed!")


def test_valid_product():
    search_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "search"))
    )
    search_box.send_keys("iPhone")
    driver.find_element(By.XPATH, "//button[@class='btn btn-default btn-lg']").click()

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "iPhone"))
    )

    assert driver.find_element(By.LINK_TEXT, "iPhone").is_displayed()
    print("Valid product search test passed!")


def test_invalid_product():
    driver.find_element(By.NAME, "search").send_keys("pulsar")
    driver.find_element(By.XPATH, "//button[@class='btn btn-default btn-lg']").click()

    expected_text = "There is no product that matches the search criteria."
    actual_text = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//p[contains(text(),'There is no product')]")
        )
    ).text

    assert expected_text in actual_text
    print("Invalid product search test passed!")


def test_no_product_found():
    driver.find_element(By.NAME, "search").send_keys("nx100")
    driver.find_element(By.XPATH, "//button[@class='btn btn-default btn-lg']").click()

    expected_text = "There is no product that matches the search criteria."
    actual_text = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//p[contains(text(),'There is no product')]")
        )
    ).text

    assert expected_text in actual_text
    print("No product found test passed!")