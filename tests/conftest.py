import pytest

from typing import Iterator, Any
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver

@pytest.fixture(params=["chrome", "firefox", "edge" ])
def driver(request: Any) -> Iterator[WebDriver]:
    browser = request.param
    #browser: str = request.config.getoption("--browser")  # USING CLI ARGs
    print(f"Creating {browser} driver")

    web_driver: WebDriver

    if browser.lower() == "edge":
        web_driver = webdriver.Edge()
    elif browser.lower() == "firefox":
        web_driver = webdriver.Firefox()
    elif browser.lower() == "chrome":
        web_driver = webdriver.Chrome()
    else:
        print(f"Browser {browser} not supported, using Chrome instead")
        web_driver = webdriver.Chrome()

    #Implicit Wait
    #web_driver.implicitly_wait(5)

    yield web_driver

    web_driver.quit()


def pytest_addoption(parser) -> None:
    parser.addoption("--browser", action="store", default="chrome", help="Type of browser: chrome, edge, or firefox")
