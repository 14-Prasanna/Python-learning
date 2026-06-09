import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.usefixtures("setup")
class TestNinja:

    def test_home_page(self):
        

        print("Current URL :", self.driver.current_url)
        print("Page Title  :", self.driver.title)

        assert "https://tutorialsninja.com/demo/index.php?route=common/home" in self.driver.current_url.lower()
        assert self.driver.title != ""
        print("Home page test passed!")

    def test_search_product(self):

    

        print("Current URL :", self.driver.current_url)
        print("Page Title  :", self.driver.title)
        
        search = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input.form-control.input-lg"))
        )
        search.clear()
        search.send_keys("HP")
        search.send_keys(Keys.ENTER)

        search_result = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[@id='content']/h1"))
        )

        assert "Search - HP" in search_result.text
        print("Search bar test passed!")

    def test_valid_product(self):

        

        print("Current URL :", self.driver.current_url)
        print("Page Title  :", self.driver.title)

        search_box = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.NAME, "search"))
        )
        search_box.clear()                          
        search_box.send_keys("iPhone")
        self.driver.find_element(By.XPATH, "//button[@class='btn btn-default btn-lg']").click()

        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, "iPhone"))
        )

        assert self.driver.find_element(By.LINK_TEXT, "iPhone").is_displayed()
        print("Valid product search test passed!")

    def test_invalid_product(self):

        


        print("Current URL :", self.driver.current_url)
        print("Page Title  :", self.driver.title)

        search_box = WebDriverWait(self.driver, 10).until(  # ← wait + clear
            EC.presence_of_element_located((By.NAME, "search"))
        )
        search_box.clear()
        search_box.send_keys("pulsar")
        self.driver.find_element(By.XPATH, "//button[@class='btn btn-default btn-lg']").click()

        expected_text = "There is no product that matches the search criteria."
        actual_text = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//p[contains(text(),'There is no product')]")
            )
        ).text

        assert expected_text in actual_text
        print("Invalid product search test passed!")

    def test_no_product_found(self):

        


        print("Current URL :", self.driver.current_url)
        print("Page Title  :", self.driver.title)

        search_box = WebDriverWait(self.driver, 10).until(  # ← wait + clear
            EC.presence_of_element_located((By.NAME, "search"))
        )
        search_box.clear()
        search_box.send_keys("nx100")
        self.driver.find_element(By.XPATH, "//button[@class='btn btn-default btn-lg']").click()

        expected_text = "There is no product that matches the search criteria."
        actual_text = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//p[contains(text(),'There is no product')]")
            )
        ).text

        assert expected_text in actual_text
        print("No product found test passed!")