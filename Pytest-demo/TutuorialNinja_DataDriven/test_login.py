import pytest
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from utilites.ExcelReader import get_data
from utilites.logCreator import log_generator


@pytest.mark.usefixtures("setup_and_teardown")
class TestLogin1:
    
    logger = log_generator()

    @pytest.mark.parametrize("username,password", get_data("Excel/Book1.xlsx", "Sheet1"))
    def test_login(self, username, password):
        self.wait.until(EC.visibility_of_element_located((By.XPATH, "//span[text()='My Account']"))).click()
        self.wait.until(EC.visibility_of_element_located((By.XPATH, "//a[text()='Login']"))).click()
        self.wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@name='email']"))).send_keys(username)
        self.wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@name='password']"))).send_keys(password)
        self.wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@value='Login']"))).click()

    @pytest.mark.search
    @pytest.mark.parametrize("product", get_data("Excel/Book1.xlsx", "search"))
    def test_search(self, product):
        self.wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Search']"))).send_keys(product)
        self.driver.find_element(By.XPATH, "//span[@class='input-group-btn']").click()
        time.sleep(5)   # Reduced sleep