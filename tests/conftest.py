import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from test_data.config import TestData

driver = None


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default=TestData.DEFAULT_BROWSER)


@pytest.fixture
def get_browser(request):
    _browser = request.config.getoption("--browser")
    return _browser


# @pytest.fixture(params=["chrome", "firefox"],scope="class")
@pytest.fixture
def get_driver(request, get_browser):
    global driver
    if get_browser == "chrome":
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    elif get_browser == "firefox":
        driver = webdriver.Firefox(executable_path=TestData.FIREFOX_EXECUTABLE_PATH)
    else:
        print("Browser Not Found For This Name: " + get_browser)

    driver.set_page_load_timeout(15)
    request.cls.driver = driver
    yield
    driver.close()