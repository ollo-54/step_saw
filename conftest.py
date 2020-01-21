import pytest
from selenium.webdriver.chrome.options import Options
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption('--browser', action='store', default='chrome', help='Choose browser: chrome or firefox')
    parser.addoption('--link', action='store', default='http://localhost:5000', help='Enter link')


@pytest.fixture(scope='session')
def browser(request):
    browser = request.config.getoption('browser')

    if browser == 'chrome':
        print('\nstart chrome browser for test ')
        options = Options()
        browser = webdriver.Chrome(options=options)

    elif browser == 'firefox':
        print('\nstart firefox browser for test ')
        fp = webdriver.FirefoxProfile()
        browser = webdriver.Firefox(firefox_profile=fp)

    else:
        print('Browser {} is not implemented yet'.format(browser))

    yield browser
    print('\nquit browser ')
    browser.quit()


@pytest.fixture(scope='function')
def link(request):
    return request.config.getoption('link')
