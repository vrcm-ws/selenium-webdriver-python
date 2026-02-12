import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from utilities.data_loader import load_json_data


@pytest.mark.login
class TestLoginPage:

    @pytest.mark.positive
    def test_positive_login(self, driver) -> None:

        url: str = "https://practicetestautomation.com/practice-test-login/"

        username_locator: str = "//input[@id='username']"
        password_locator: str = "//input[@id='password']"
        submit_button_locator: str = "//button[@id='submit']"
        post_message_locator: str = "//strong[contains(text(),'Congratulations')]"
        logout_locator: str = "//a[contains(text(),'Log out')]"

        wait: WebDriverWait
        web_element: WebElement

        student: str = "student"
        password: str = "Password123"

        driver = webdriver.Edge()
        wait = WebDriverWait(driver, 10)

        #Open page
        driver.get(url)

        #Type username student into Username field
        web_element = driver.find_element(By.XPATH, username_locator)
        web_element.send_keys(student)

        #Type password Password123 into Password field
        web_element = driver.find_element(By.XPATH, password_locator)
        web_element.send_keys(password)

        #Push Submit button
        driver.find_element(By.XPATH, submit_button_locator).click()

        #Verify new page URL contains practicetestautomation.com/logged-in-successfully/
        expected_url: str = "https://practicetestautomation.com/logged-in-successfully/"
        actual_url: str = driver.current_url

        assert actual_url == expected_url

        #Verify new page contains expected text ('Congratulations' or 'successfully logged in')
        expected_message: str = "Congratulations student. You successfully logged in!"
        web_element = driver.find_element(By.XPATH, post_message_locator)

        assert web_element.text == expected_message

        #Verify button Log out is displayed on the new page
        web_element = wait.until(expected_conditions.visibility_of_element_located((By.XPATH, logout_locator)))
        #web_element = driver.find_element(By.XPATH, logout_locator)

        assert web_element.is_displayed()

        driver.quit()


    @pytest.mark.negative
    @pytest.mark.parametrize("username, password, expected_message", load_json_data("test_login_data.json"))
    def test_negative_login(self, driver, username: str, password: str, expected_message: str) -> None:

        url: str = "https://practicetestautomation.com/practice-test-login/"

        username_locator: str = "//input[@id='username']"
        password_locator: str = "//input[@id='password']"
        submit_button_locator: str = "//button[@id='submit']"
        error_message_locator: str = "//div[@id='error']"

        wait: WebDriverWait
        web_element: WebElement

        wait = WebDriverWait(driver, 10)

        # Open page
        driver.get(url)

        # Type username student into Username field
        web_element = driver.find_element(By.XPATH, username_locator)
        web_element.send_keys(username)

        # Type password Password123 into Password field
        web_element = driver.find_element(By.XPATH, password_locator)
        web_element.send_keys(password)

        # Push Submit button
        driver.find_element(By.XPATH, submit_button_locator).click()

        #Verify error message is displayed
        #web_element = driver.find_element(By.XPATH, error_message_locator)
        web_element = wait.until(expected_conditions.visibility_of_element_located((By.XPATH, error_message_locator)))
        assert web_element.is_displayed()

        #Verify error message text is Your username is invalid!
        assert web_element.text == expected_message
