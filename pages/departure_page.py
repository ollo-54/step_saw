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

# первый вариант - через количество символов (можно же title?)
    def should_be_departure_header(self):
        header_len = len('Летим из ')
        departure_header  = self.browser.find_element(*DeparturePageLocators.DEPARTURE_HEADER).text
        departure_header_len = len(departure_header)
        print(departure_header)
        assert header_len != departure_header_len, 'No departure in the title'

# второй вариант - через регулярные выражения

    def get_header(self):
        departure_header = self.is_element_present(*DeparturePageLocators.DEPARTURE_HEADER)
        assert departure_header, 'This is not a header in departure page'
        departure_header_text = self.browser.find_element(*DeparturePageLocators.DEPARTURE_HEADER).text
        return departure_header_text

    def should_be_departure_header1(self, departure_header):
        print(departure_header)
        departure_header_text = re.search(r'Летим Из \w+', departure_header)
        print(departure_header_text)
        assert departure_header_text, 'No departure in the header'

# ===========================================

    def get_description(self):
        departure_description = self.is_element_present(*DeparturePageLocators.CARDS_IN_DESCRIPTION)
        assert departure_description, 'This is not a description in departure page'
        departure_description_text = self.browser.find_element(*DeparturePageLocators.CARDS_IN_DESCRIPTION).text
        return departure_description_text

    def should_be_cards_in_description(self, departure_description):
        print(departure_description)
        departure_description_text = re.search(r'Найдено \d туров', departure_description)
        print(departure_description_text)
        assert departure_description_text, 'No amount cards in description'

    def should_be_cards_in_description2(self, departure_description):
        print(departure_description)
        link_on_card = self.browser.find_elements(*MainPageLocators.LINK_ON_CARD)
        amount_of_cards_with_link = len(link_on_card)
        departure_description_text = 'Найдено ' + str(amount_of_cards_with_link) + ' туров'
        print(departure_description_text)
        assert departure_description_text in departure_description, 'No departure in the header'

    def should_be_price_in_description(self, departure_description):
        print(departure_description)
        departure_description_text = re.search(r'от \d{1,} до \d{1,} и', departure_description)
        print(departure_description_text)
        assert departure_description_text, 'Price is not indicated in the description'        

    def should_be_days_in_description(self, departure_description):
        print(departure_description)
        departure_description_text = re.search(r'от \d{1,} ночей до \d{1,} ночей', departure_description)
        print(departure_description_text)
        assert departure_description_text, 'Days is not indicated in the description'

