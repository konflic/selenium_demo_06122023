import os.path

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.service import Service as FFService
from selenium.webdriver.firefox.options import Options as FFOptions
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.safari.service import Service as SafariService
import pytest


def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--base_url")
    parser.addoption("--headless", action="store_true")
    parser.addoption("--ya_driver")


@pytest.fixture(scope="session")
def base_url(request):
    return request.config.getoption("--base_url")


@pytest.fixture()
def browser(request, base_url):
    browser_name = request.config.getoption("--browser")
    headless = request.config.getoption("--headless")
    ya_driver = request.config.getoption("--ya_driver")

    _browser = None

    if browser_name == "chrome":
        service = ChromeService()
        options = ChromeOptions()
        if headless:
            options.add_argument("headless=new")
        _browser = webdriver.Chrome(service=service, options=options)
    elif browser_name == "ff":
        service = FFService()
        options = FFOptions()
        if headless:
            options.add_argument("-headless")
        _browser = webdriver.Firefox(service=service, options=options)
    elif browser_name == "edge":
        service = EdgeService()
        options = ChromeOptions()
        if headless:
            options.add_argument("headless=new")
        _browser = webdriver.Edge(service=service, options=options)
    elif browser_name == "ya":
        options = ChromeOptions()
        if headless:
            options.add_argument("headless=new")
        service = ChromeService(executable_path=f'{ya_driver}/yandexdriver')
        _browser = webdriver.Chrome(service=service, options=options)
    elif browser_name == "safari":
        service = SafariService()
        _browser = webdriver.Safari(service=service)

    _browser.maximize_window()
    _browser.base_url = base_url

    yield _browser

    _browser.close()
