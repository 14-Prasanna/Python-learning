import pytest
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

from utilites.ExcelReader import get_data
from utilites.logCreator import log_generator


@pytest.mark.usefixtures("setup_and_teardown")
class TestLogin1:

    logger = log_generator


    @pytest.mark.run(order=2)
    @pytest.mark.dependency(depends=["test_login"])
    @pytest.mark.search
    @pytest.mark.parametrize("product", get_data("Excel/Book1.xlsx", "search"))
    def test_search(self, product):
        
        if isinstance(product, (list, tuple)):
            product = product[0]
        product = str(product).strip()

        self.logger.info(f"Starting test_search with product='{product}'")

        
        self.wait.until(
            EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Search']"))
        ).send_keys(product)
        self.driver.find_element(By.XPATH, "//span[@class='input-group-btn']").click()

        
        try:
            self.wait.until(
                EC.visibility_of_element_located((By.XPATH, "//div[@id='content']"))
            )
        except TimeoutException:
            self.logger.error(f"Search results page did not load for product='{product}'")
            pytest.fail(f"Search results page did not load for product='{product}'")

        
        try:
            self.wait.until(
                EC.visibility_of_element_located(
                    (By.XPATH, "//h2[text()='Products meeting the search criteria']")
                )
            )
        except TimeoutException:
            self.logger.error(f"Search results page heading not found for product='{product}'")
            pytest.fail(f"Search results page did not render for product='{product}'")

        
        product_cards = self.driver.find_elements(
            By.XPATH, "//div[@id='content']//div[contains(@class,'product-layout')]"
        )

        if len(product_cards) > 0:
            
            self.logger.info(
                f"Search SUCCESS — product='{product}' | {len(product_cards)} result(s) found."
            )

        else:
            
            try:
                no_result_msg = self.wait.until(
                    EC.visibility_of_element_located(
                        (By.XPATH, "//p[contains(text(),'There is no product that matches the search criteria')]")
                    )
                ).text

                assert "There is no product that matches the search criteria" in no_result_msg, \
                    f"Unexpected no-results message for product='{product}': '{no_result_msg}'"

                self.logger.warning(
                    f"Search returned no results for product='{product}': '{no_result_msg}'"
                )

            except TimeoutException:
                self.logger.error(
                    f"No product cards and no no-results message found for product='{product}'"
                )
                pytest.fail(
                    f"Search page shows neither results nor a no-results message for product='{product}'"
                )



    @pytest.mark.run(order=1)
    @pytest.mark.parametrize("username,password", get_data("Excel/Book1.xlsx", "Sheet1"))
    def test_login(self, username, password):
        self.logger.info(f"Starting test_login with username='{username}'")

        
        self.wait.until(
            EC.visibility_of_element_located((By.XPATH, "//span[text()='My Account']"))
        ).click()
        self.wait.until(
            EC.visibility_of_element_located((By.XPATH, "//a[text()='Login']"))
        ).click()

        
        self.wait.until(
            EC.visibility_of_element_located((By.XPATH, "//input[@name='email']"))
        ).send_keys(username)
        self.wait.until(
            EC.visibility_of_element_located((By.XPATH, "//input[@name='password']"))
        ).send_keys(password)
        self.wait.until(
            EC.visibility_of_element_located((By.XPATH, "//input[@value='Login']"))
        ).click()

        
        try:
            warning_elem = self.wait.until(
                EC.visibility_of_element_located(
                    (By.XPATH, "//div[text()='Warning: No match for E-Mail Address and/or Password.']")
                )
            )
            warning_text = warning_elem.text
            self.logger.warning(
                f"Invalid login attempt — username='{username}' | Warning: '{warning_text}'"
            )
            assert "Warning: No match for E-Mail Address and/or Password." in warning_text, \
                f"Unexpected warning message displayed: '{warning_text}'"
            self.logger.info("Invalid login handled correctly.")
            return 

        except TimeoutException:
            pass 

        
        try:
            account_heading = self.wait.until(
                EC.visibility_of_element_located(
                    (By.XPATH, "//div[@id='content']//h2[text()='My Account']")
                )
            ).text
        except TimeoutException:
            self.logger.error(f"Login failed for username='{username}': 'My Account' heading not found.")
            pytest.fail(f"Login unsuccessful for username='{username}'")

        assert "My Account" in account_heading, \
            f"Login unsuccessful for username='{username}'. Page heading: '{account_heading}'"
        self.logger.info(f"Login successful for username='{username}'")

        
        try:
            self.driver.find_element(By.XPATH, "//aside//a[text()='Logout']").click()
        except Exception as e:
            self.logger.error(f"Logout link not found: {e}")
            pytest.fail("Logout link not found on My Account page.")

        try:
            logout_heading = self.wait.until(
                EC.visibility_of_element_located(
                    (By.XPATH, "//div[@id='content']//h1")
                )
            ).text
        except TimeoutException:
            self.logger.error("Logout page heading not found after clicking Logout.")
            pytest.fail("Logout failed: confirmation heading not found.")

        
        assert "Account Logout" in logout_heading, \
            f"Logout failed. Page heading: '{logout_heading}'"
        self.logger.info(f"Logout successful for username='{username}'")

        
        self.driver.find_element(By.XPATH, "//div[@class='buttons']//a").click()
        self.logger.info(f"Redirected to: {self.driver.current_url}")