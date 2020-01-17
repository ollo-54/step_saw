from pages.base_page import BasePage
from pages.locators import MainPageLocators
from pages.locators import DeparturePageLocators
from pages.locators import TourPageLocators
import re

class DeparturePage(BasePage):

    def should_be_departure_page(self):
        departure_header = self.is_element_present(*DeparturePageLocators.DEPARTURE_HEADER)
        assert departure_header, 'No go to departure page'
        current_url_departure = self.browser.current_url
        print('Current url departure', current_url_departure)
        assert 'departure' in current_url_departure, f"This is not departure page, expected 'departure' in the {current_url_departure}"

    def get_header_text(self):
        departure_header = self.is_element_present(*DeparturePageLocators.DEPARTURE_HEADER)
        assert departure_header, 'This is not a header in departure page'
        departure_header_text = self.browser.find_element(*DeparturePageLocators.DEPARTURE_HEADER).text
        return departure_header_text

    def get_departure_description_text(self):
        departure_description = self.is_element_present(*DeparturePageLocators.DEPARTURE_DESCRIPTION)
        assert departure_description, 'This is not a description in departure page'
        departure_description_text = self.browser.find_element(*DeparturePageLocators.DEPARTURE_DESCRIPTION).text
        return departure_description_text

    def get_amount_of_tour_cards(self):
        link_on_tour_cards = self.browser.find_elements(*MainPageLocators.LINK_ON_TOUR_CARD)
        amount_of_tour_cards_with_link = len(link_on_tour_cards)
        print('Amount of tour cards per page ' + str(amount_of_tour_cards_with_link))
        return amount_of_tour_cards_with_link

