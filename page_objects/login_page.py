from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from page_objects.base_page import BasePage
from page_objects.login_page_confirmation import LoginPageConfirmation


class LoginPage(BasePage):

    __page_url: str = "https://practicetestautomation.com/practice-test-login/"
    __username_field: tuple[str, str] = (By.XPATH, "//input[@id='username']")
    __password_field: tuple[str, str] = (By.XPATH, "//input[@id='password']")
    __submit_button: tuple[str, str] = (By.XPATH, "//button[@id='submit']")
    __error_message_locator: tuple[str, str] = (By.XPATH, "//div[@id='error']")

    __username: str = "student"
    __password: str = "Password123"


    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver)


    def load_page(self) -> None:
        self._driver.get(self.__page_url)


    def enter_username(self, username: str) -> None:
        self._type_element(self.__username_field, username)


    def enter_password(self, password: str) -> None:
        self._type_element(self.__password_field, password)


    def click_submit(self) -> None:
        self._click_element(self.__submit_button)


    def login(self) -> LoginPageConfirmation:
        self.enter_username(self.__username)
        self.enter_password(self.__password)
        self.click_submit()

        return LoginPageConfirmation(self._driver)


    def is_error_message_displayed(self) -> bool:
        return self._is_element_displayed(self.__error_message_locator)


    def get_error_message(self) -> str:
        return self._get_element_text(self.__error_message_locator)



