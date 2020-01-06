import pytest
from selenium.webdriver.chrome.options import Options
from selenium import webdriver

<<<<<<< HEAD
def pytest_addoption(parser):
    parser.addoption('--browser', action='store', default="chrome", help="Choose browser: chrome or firefox")

=======

def pytest_addoption(parser):
    parser.addoption('--browser', action='store', default="chrome", help="Choose browser: chrome or firefox")


>>>>>>> d42005df3da7e08d61e91e312fb2f442b5ef2fa0
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
<<<<<<< HEAD
    browser.quit()
=======
    browser.quit()
>>>>>>> d42005df3da7e08d61e91e312fb2f442b5ef2fa0
