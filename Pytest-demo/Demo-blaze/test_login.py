import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from resources.ConfigReader import get_value


@pytest.mark.usefixtures("setup")
class TestLogin:

    def test_login_with_valid(self):

        print("Current URL :", self.driver.current_url)
        print("Page Title  :", self.driver.title)

        username = get_value("Login Info", "username")
        password = get_value("Login Info", "password")

        
        self.driver.find_element(By.ID, "login2").click()

        
        self.wait.until(
            EC.visibility_of_element_located((By.ID, "loginusername"))
        ).send_keys(username)

        
        self.driver.find_element(By.ID, "loginpassword").send_keys(password)

        
        self.driver.find_element(By.XPATH, "//button[text()='Log in']").click()

        
        check_username = self.wait.until(
            EC.visibility_of_element_located((By.ID, "nameofuser"))
        ).text

        assert username in check_username

        print("Login successful")