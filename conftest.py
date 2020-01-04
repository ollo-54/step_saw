import pytest
from selenium.webdriver.chrome.options import Options
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption('--browser', action='store', default="chrome", help="Choose browser: chrome or firefox")


@pytest.fixture(scope="function")
def browser(request):
    browser = request.config.getoption("browser")

    if browser == "chrome":
        print("\nstart chrome browser for test ")
        options = Options()
        browser = webdriver.Chrome(options=options)

    elif browser == "firefox":
        print("\nstart firefox browser for test ")
        fp = webdriver.FirefoxProfile()
        browser = webdriver.Firefox(firefox_profile=fp)

    else:
        print("Browser {} still is not implemented".format(browser_name))

    yield browser
    print("\nquit browser ")
    browser.quit()
