from pages.base_page import BasePage
from pages.locators import MainPageLocators
import time

class MainPage(BasePage):
    def should_be_main_page_link_on_logo(self):
        button = self.browser.find_element(*MainPageLocators.LOGO_LINK).get_attribute('href')
        print('Link - ' + str(button))
        assert button == 'https://stepik-flask01.herokuapp.com/', 'There is no link to the main page on the logo'

    def should_be_menu_on_page(self):
        menu_main = self.is_element_present(*MainPageLocators.MENU_ON_PAGE)
        assert menu_main, 'Menu is not on the page'

    def should_be_cards_on_page(self):
        cards = self.browser.find_elements(*MainPageLocators.CARDS)
        amount_cards = len(cards)
        print('Amount of cards per page ' + str(amount_cards))
        assert amount_cards >= 3, 'Less than three cards per page'
    
    def links_lead_to_different_pages(self):
        menu_items = self.browser.find_elements(*MainPageLocators.MENU_ITEMS)
        amount_of_menu_items = len(menu_items)
        print('Amount of menu items ' + str(amount_of_menu_items))
        i = 0
        list_of_links = []
        for element in menu_items:
            new_link = element.get_attribute('href')
            list_of_links.append(new_link)
            print('Link # ' + str(i) + '\n' + new_link)
            i = i + 1
        list_of_links_set = set(list_of_links)
        print('Total ' + str(len(list_of_links)) + ' links, ' + str(len(list_of_links_set)) + ' of which are unique')
        assert len(list_of_links) == len(list_of_links_set), 'Duplicate links'            

    def cards_have_different_pictures(self):
        picture_on_card = self.browser.find_elements(*MainPageLocators.PICTURE_ON_CARD)
        amount_of_cards_with_picture = len(picture_on_card)
        print('Amount of cards with pictures ' + str(amount_of_cards_with_picture))
        i = 0
        list_of_pictures = []
        for element in picture_on_card:
            new_picture = element.get_attribute("src")
            print('Picture # ' + str(i) + '\n' + new_picture)
            list_of_pictures.append(new_picture)
            i = i + 1
        list_of_pictures_set = set(list_of_pictures)
        print('Total ' + str(len(list_of_pictures)) + ' pictures, ' + str(len(list_of_pictures_set)) + ' of which are unique')
        assert len(list_of_pictures) == len(list_of_pictures_set), 'Duplicate pictures'

    def cards_have_different_content(self):
        content_on_card = self.browser.find_elements(*MainPageLocators.CONTENT_ON_CARD)
        amount_of_cards_with_content = len(content_on_card)
        print('Amount of cards with content ' + str(amount_of_cards_with_content))
        i = 0
        list_of_content = []
        for element in content_on_card:
            new_content = element.text
            list_of_content.append(new_content)
            print('Content # ' + str(i) + '\n' + new_content)
            i = i + 1
        list_of_content_set = set(list_of_content)
        print('Total ' + str(len(list_of_content)) + ' contents, ' + str(len(list_of_content_set)) + ' of which are unique')
        assert len(list_of_content) == len(list_of_content_set), 'Duplicate content'

    def cards_have_different_links(self):
        link_on_card = self.browser.find_elements(*MainPageLocators.LINK_ON_CARD)
        amount_of_cards_with_link = len(link_on_card)
        print('Amount of cards with link ' + str(amount_of_cards_with_link))
        i = 0
        list_of_links = []
        for element in link_on_card:
            new_link = element.get_attribute('href')
            list_of_links.append(new_link)
            print('Link # ' + str(i) + '\n' + new_link)
            i = i + 1 
        list_of_links_set = set(list_of_links)
        print('Total ' + str(len(list_of_links)) + ' links, ' + str(len(list_of_links_set)) + ' of which are unique')
        assert len(list_of_links) == len(list_of_links_set), 'Links do not lead to internal pages'

    def click_on_the_departure_link(self):
        menu_item = self.browser.find_element(*MainPageLocators.MENU_ITEMS)
        menu_item.click()
        transition_check_departure = self.browser.find_element(*MainPageLocators.TRANSITION_CHECK_DEPARTURE).text
        assert 'Летим Из' in transition_check_departure, 'No go to departure page'

    def should_be_departure_page(self):
        assert 'departure' in self.browser.current_url, 'The link does not lead to the departure page'
        
    def click_on_the_tour_link(self):
        card_link = self.browser.find_element(*MainPageLocators.LINK_ON_CARD)
        card_link.click()
        transition_check_tour = self.browser.find_element(*MainPageLocators.TRANSITION_CHECK_TOUR).text
        assert transition_check_tour, 'No go to tour page'

    def should_be_tour_page(self):
        assert 'tour' in self.browser.current_url, 'The link does not lead to the tour page'
        

