from selenium.common import TimeoutException
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver: WebDriver) -> None:
        self._driver: WebDriver = driver
        self._wait: WebDriverWait = WebDriverWait(self._driver, 10, 0.1)


    #Protected methods
    def _wait_for_element(self, locator: tuple[str, str]) -> WebElement:
        return self._wait.until(ec.visibility_of_element_located(locator))


    def _find_element(self, locator: tuple[str, str]) -> WebElement:
        return self._wait_for_element(locator)


    def _find_elements(self, locator: tuple[str, str]) -> list[WebElement]:
        return self._wait.until(ec.visibility_of_all_elements_located(locator))


    def _click_element(self, locator: tuple[str, str]) -> None:
        self._wait_for_element(locator).click()


    def _type_element(self, locator: tuple[str, str], text_to_type: str) -> None:
        self._wait_for_element(locator).send_keys(text_to_type)


    def _get_element_text(self, locator: tuple[str, str]) -> str:
        return self._wait_for_element(locator).text


    def _is_element_displayed(self, locator: tuple[str, str]) -> bool:
        try:
            return self._wait_for_element(locator).is_displayed()
        except TimeoutException:
            return False

    #Public methods
    def get_page_url(self) -> str:
        return self._driver.current_url