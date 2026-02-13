import pytest

from page_objects.login_page import LoginPage
from page_objects.login_page_confirmation import LoginPageConfirmation
from utilities.data_loader import load_json_data


@pytest.mark.login
class TestLoginPage:

    @pytest.mark.positive
    def test_positive_login(self, driver) -> None:

        login_page: LoginPage = LoginPage(driver)
        login_page.load_page()

        confirmation_page: LoginPageConfirmation = login_page.login()

        assert confirmation_page.current_url == confirmation_page.expected_url
        assert confirmation_page.confirmation_message == "Congratulations student. You successfully logged in!"
        assert confirmation_page.is_logout_button_displayed


    @pytest.mark.negative
    @pytest.mark.parametrize("username, password, expected_message", load_json_data("test_login_data.json"))
    def test_negative_login(self, driver, username: str, password: str, expected_message: str) -> None:

        login_page: LoginPage = LoginPage(driver)
        login_page.load_page()

        login_page.enter_username(username)
        login_page.enter_password(password)
        login_page.click_submit()

        assert login_page.is_error_message_displayed()
        assert login_page.get_error_message() == expected_message
