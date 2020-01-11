from pages.base_page import BasePage
from pages.locators import DeparturePageLocators

class DeparturePage(BasePage):

    def should_be_departure_page(self):
        departure_header = self.is_element_present(*DeparturePageLocators.DEPARTURE_HEADER)
        assert departure_header, 'No go to departure page'
        current_url_departure = self.browser.current_url
        print('Current url departure', current_url_departure)
        assert 'departure' in current_url_departure, f"This is not departure page, expected 'departure' in the {current_url_departure}"


 

 
