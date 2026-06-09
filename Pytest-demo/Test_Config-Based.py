import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

from resources.ConfigReader import get_value


def setup_function(function):
    global driver

    url = get_value("Basic Info", "url")

    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get(url)


def teardown_function(function):
    driver.quit()


def test_home_page():

    print("Current URL :", driver.current_url)
    print("Page Title  :", driver.title)

    url = get_value("Basic Info", "url")

    assert url in driver.current_url
    assert driver.title != ""

    print("Home page test passed!")


def test_search_product():

    key = get_value("search items", "key")

    search = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "input.form-control.input-lg"))
    )

    search.clear()
    search.send_keys(key)
    search.send_keys(Keys.ENTER)

    search_result = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[@id='content']/h1"))
    )

    assert f"Search - {key}" in search_result.text

    print("Search bar test passed!")


def test_valid_product():

    product = get_value("search items", "valid_product")

    search_box = driver.find_element(By.NAME, "search")
    search_box.clear()
    search_box.send_keys(product)

    driver.find_element(By.XPATH, "//button[@class='btn btn-default btn-lg']").click()

    iphone = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, product))
    )

    assert iphone.is_displayed()

    print("Valid product search test passed!")


def test_invalid_product():

    product = get_value("search items", "invalid_product")

    search_box = driver.find_element(By.NAME, "search")
    search_box.clear()
    search_box.send_keys(product)

    driver.find_element(By.XPATH, "//button[@class='btn btn-default btn-lg']").click()

    text = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//p[contains(text(),'There is no product')]"))
    ).text

    assert "There is no product" in text

    print("Invalid product search test passed!")


def test_no_product_found():

    product = get_value("search items", "no_product")

    search_box = driver.find_element(By.NAME, "search")
    search_box.clear()
    search_box.send_keys(product)

    driver.find_element(By.XPATH, "//button[@class='btn btn-default btn-lg']").click()

    text = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//p[contains(text(),'There is no product')]"))
    ).text

    assert "There is no product" in text

    print("No product found test passed!")