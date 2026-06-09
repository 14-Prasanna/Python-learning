import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from utilities import logCreation
from utilities import excelData




@pytest.mark.usefixtures("setup")
@pytest.mark.parametrize(
    "username,password",
    excelData.get_data("Excelfiles\\loginData.xlsx", "login")
)
def test_login_with_valid(setup, username, password):

    driver, wait = setup

    logger = logCreation.log_generator()
    logger.info("Current URL : %s", driver.current_url)
    logger.info("Page Title : %s", driver.title)

    wait.until(
        EC.visibility_of_element_located((By.ID, "login2"))
    )

    driver.find_element(By.ID, "login2").click()

    wait.until(
        EC.visibility_of_element_located((By.ID, "loginusername"))
    ).send_keys(username)

    driver.find_element(By.ID, "loginpassword").send_keys(password)

    driver.find_element( By.XPATH,"//button[text()='Log in']").click()

    try:
        alert = wait.until(EC.alert_is_present())
        logger.info("Login failed : %s", alert.text)

        assert alert.text in ["Wrong password.", "User does not exist."]

        
        alert.accept()

    except TimeoutException:
        logger.info("Login successful for user : %s", username)
        check_username = wait.until(EC.visibility_of_element_located((By.ID, "nameofuser"))).text

        assert username in check_username   
        logger.info("Login successful for user : %s", username)

        driver.find_element(By.XPATH, "//a[text()='Log out']").click()