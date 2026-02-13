from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from page_objects.base_page import BasePage


class LoginPageConfirmation(BasePage):

    _page_url: str = "https://practicetestautomation.com/logged-in-successfully/"

    __message_locator: tuple[str, str] = (By.XPATH, "//strong[contains(text(),'Congratulations')]")
    __logout_button_locator: tuple[str, str] = (By.XPATH, "//a[contains(text(),'Log out')]")

    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver)


    @property
    def current_url(self) -> str:
        return self._driver.current_url

    @property
    def expected_url(self) -> str:
        return self._page_url

    @property
    def confirmation_message(self) -> str:
        return self._get_element_text(self.__message_locator)

    @property
    def is_logout_button_displayed(self) -> bool:
        return self._is_element_displayed(self.__logout_button_locator)


