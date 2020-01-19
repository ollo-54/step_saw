from pages.base_page import BasePage
from pages.locators import TourPageLocators
from pages.locators import DeparturePageLocators


class TourPage(BasePage):        

    def should_be_tour_page(self):
        tour_header = self.is_element_present(*TourPageLocators.TOUR_HEADER)
        assert tour_header, 'No go to tour page'
        current_url_tour = self.browser.current_url
        print('Current url tour', current_url_tour)
        assert 'tour' in current_url_tour, f"This is not tour page, expected 'tour' in the {current_url_tour}"

    def should_be_departure_tour_title(self):
        departure_tour_title_text = self.browser.find_element(*DeparturePageLocators.DEPARTURE_TOUR_TITLE).text
        return departure_tour_title_text

    def should_be_tour_title(self):
        tour_title_text = self.browser.find_element(*TourPageLocators.TOUR_TITLE).text
        return tour_title_text

    def should_be_tour_duration_of_stay(self):
        tour_duration_of_stay = self.browser.find_element(*TourPageLocators.TOUR_DESCRIPTION).text
        return tour_duration_of_stay

    def should_be_tour_price(self):
        tour_price_text = self.browser.find_element(*TourPageLocators.TOUR_PRICE).text
        return tour_price_text
