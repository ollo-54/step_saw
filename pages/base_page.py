from selenium.common.exceptions import NoSuchElementException
from pages.locators import MainPageLocators
#from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait

class BasePage():
    def __init__(self, browser, url, timeout=3):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True
