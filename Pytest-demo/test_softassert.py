import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get("https://tutorialsninja.com/demo/index.php?route=common/home")
    yield driver
    driver.quit()



def test_home_page(driver):

    print("Current URL :", driver.current_url)
    print("Page Title  :", driver.title)

    page = driver.title()

    assert "tutorialsninja.com" in driver.current_url.lower()
    assert driver.title != ""

    assert page in driver.title


    print("Home page test passed!")


def test_search_product(driver):

    print("Current URL :", driver.current_url)
    print("Page Title  :", driver.title)

    search = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, "input.form-control.input-lg")
        )
    )

    search.clear()
    search.send_keys("HP")
    search.send_keys(Keys.ENTER)

    search_result = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//div[@id='content']/h1")
        )
    )

    assert "Search - HP" in search_result.text

    print("Search bar test passed!")



def test_valid_product(driver):

    search_box = driver.find_element(By.NAME, "search")
    search_box.clear()
    search_box.send_keys("iPhone")

    driver.find_element(By.XPATH, "//button[@class='btn btn-default btn-lg']").click()

    iphone = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "iPhone"))
    )

    assert iphone.is_displayed()


def test_invalid_product(driver):

    search_box = driver.find_element(By.NAME, "search")
    search_box.clear()
    search_box.send_keys("pulsar")

    driver.find_element(By.XPATH, "//button[@class='btn btn-default btn-lg']").click()

    text = driver.find_element(
        By.XPATH, "//p[contains(text(),'There is no product')]"
    ).text

    assert "There is no product" in text


def test_no_product_found(driver):

    search_box = driver.find_element(By.NAME, "search")
    search_box.clear()
    search_box.send_keys("nx100")

    driver.find_element(By.XPATH, "//button[@class='btn btn-default btn-lg']").click()

    text = driver.find_element(
        By.XPATH, "//p[contains(text(),'There is no product')]"
    ).text

    assert "There is no product" in text