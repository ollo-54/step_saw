from pages.base_page import BasePage
#from pages.locators import MainPageLocators
#from pages.locators import DeparturePageLocators
from pages.locators import TourPageLocators


class TourPage(BasePage):        

    def should_be_tour_page(self):
        tour_header = self.is_element_present(*TourPageLocators.TOUR_HEADER)
        assert tour_header, 'No go to tour page'
        current_url_tour = self.browser.current_url
        print('Current url tour', current_url_tour)
        assert 'tour' in current_url_tour, f"This is not tour page, expected 'tour' in the {current_url_tour}"
        
        