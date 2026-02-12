import pytest
from selenium.common import TimeoutException, InvalidElementStateException, StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.exception
class TestExceptionsPage:

    def test_no_such_element_exception(self, driver) -> None:

        page_url: str = "https://practicetestautomation.com/practice-test-exceptions/"

        #locators
        add_button_locator: str = "//button[@id='add_btn']"
        row2_input_locator: str = "//div[@id='row2']/input"

        element: WebElement
        wait: WebDriverWait = WebDriverWait(driver, 10)

        driver.get(page_url)
        driver.find_element(By.XPATH, add_button_locator).click()

        #This trigger the exception
        #element = driver.find_element(By.XPATH, row2_input_locator)

        element = wait.until(expected_conditions.visibility_of_element_located((By.XPATH, row2_input_locator)))

        assert element.is_displayed() == True

    @pytest.mark.exception
    def test_element_not_interactable_exception(self, driver) -> None:

        page_url: str = "https://practicetestautomation.com/practice-test-exceptions/"

        #locators
        add_button_locator: str = "//button[@id='add_btn']"
        save_button_locator: str = "//button[@id='save_btn']"
        row2_input_locator: str = "//div[@id='row2']/input"
        confirmation_message_locator: str = "//div[@id='confirmation']"

        element: WebElement
        wait: WebDriverWait = WebDriverWait(driver, 10)

        driver.get(page_url)
        driver.find_element(By.XPATH, add_button_locator).click()

        element = wait.until(expected_conditions.visibility_of_element_located((By.XPATH, row2_input_locator)))
        element.send_keys("Test Text")

        #Triggers exception
        #driver.find_element(By.XPATH, f"({save_button_locator})[1]").click()

        driver.find_element(By.XPATH, f"({save_button_locator})[2]").click()

        element = wait.until(expected_conditions.visibility_of_element_located((By.XPATH, confirmation_message_locator)))

        assert element.is_displayed() == True, "Confirmation Text should have been displayed"

    @pytest.mark.exception
    def test_invalid_element_state_exception(self, driver) -> None:

        page_url: str = "https://practicetestautomation.com/practice-test-exceptions/"

        #locators
        row1_input_locator: str = "//div[@id='row1']/input"
        row1_edit_button_locator: str = "//div[@id='row1']/button[text()='Edit']"
        row1_save_button_locator: str = "//div[@id='row1']/button[text()='Save']"
        confirmation_message_locator: str = "//div[@id='confirmation']"

        element: WebElement
        wait: WebDriverWait = WebDriverWait(driver, 10)

        driver.get(page_url)

        # # Triggers exception
        # try:
        #     #driver.find_element(By.XPATH, row1_input_locator).clear()
        #
        # except InvalidElementStateException as e:
        #     print(e)

        test_text: str = "New Test Text"

        driver.find_element(By.XPATH, row1_edit_button_locator).click()
        element = wait.until(expected_conditions.element_to_be_clickable((By.XPATH, row1_input_locator)))
        element.send_keys(test_text)

        driver.find_element(By.XPATH, row1_save_button_locator).click()
        element = wait.until(expected_conditions.visibility_of_element_located((By.XPATH, confirmation_message_locator)))

        assert element.text == "Row 1 was saved", "Confirmation Text should have been displayed"

        driver.quit()


    @pytest.mark.exception
    def test_stale_element_reference_exception(self, driver) -> None:

        page_url: str = "https://practicetestautomation.com/practice-test-exceptions/"

        #locators
        instructions_locator: str = "//p[@id='instructions']"
        row1_add_button_locator: str = "//div[@id='row1']/button[text()='Add']"

        element: WebElement
        wait: WebDriverWait = WebDriverWait(driver, 10)

        driver.get(page_url)

        element = driver.find_element(By.XPATH, instructions_locator)

        driver.find_element(By.XPATH, row1_add_button_locator).click()

        # #Triggers exception
        # try:
        #     assert element.is_displayed()
        #
        # except StaleElementReferenceException as e:
        #     print(e)

        assert wait.until(expected_conditions.invisibility_of_element_located((By.XPATH, instructions_locator)))

        driver.quit()


