from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import MainPageLocators
import time

<<<<<<< HEAD
class MainPage(BasePage):
    def should_be_main_page_link_on_logo(self):
        button = self.browser.find_element(*MainPageLocators.LOGO_LINK)
        assert button, "Does not go to the main page when clicking on the logo"

    def should_be_menu_on_page(self):
        menu_main = self.is_element_present(*MainPageLocators.MENU_ON_PAGE)
        assert menu_main, 'Menu is not on the page'

    def should_be_cards_on_page(self):
        cards = self.browser.find_elements(*MainPageLocators.CARDS)
        amount_cards = len(cards)
        print("Amount of cards per page " + str(amount_cards))
        assert amount_cards >= 3, 'Less than three cards per page'
    
    def links_lead_to_different_pages(self):
        menu_items = self.browser.find_elements(*MainPageLocators.MENU_ITEMS)
        amount_of_menu_items = len(menu_items)
        print("Amount of menu items " + str(amount_of_menu_items))
        i = 0
        list_of_links = []
        for element in menu_items:
            new_link = element.get_attribute("href")
            list_of_links.append(new_link)
            print("Link # " + str(i) + "\n" + new_link)
            i = i + 1
        list_of_links_set = set(list_of_links)
        print("Total " + str(len(list_of_links)) + " links, " + str(len(list_of_links_set)) + " of which are unique")
        assert len(list_of_links) == len(list_of_links_set), 'Duplicate links'            

    def cards_have_different_pictures(self):
        picture_on_card = self.browser.find_elements(*MainPageLocators.PICTURE_ON_CARD)
        amount_of_cards_with_picture = len(picture_on_card)
        print("Amount of cards with pictures " + str(amount_of_cards_with_picture))
        i = 0
        list_of_pictures = []
        for element in picture_on_card:
            new_picture = element.get_attribute("src")
            print("Picture # " + str(i) + "\n" + new_picture)
            list_of_pictures.append(new_picture)
            i = i + 1
        list_of_pictures_set = set(list_of_pictures)
        print("Total " + str(len(list_of_pictures)) + " pictures, " + str(len(list_of_pictures_set)) + " of which are unique")
        assert len(list_of_pictures) == len(list_of_pictures_set), 'Duplicate pictures'

    def cards_have_different_content(self):
        content_on_card = self.browser.find_elements(*MainPageLocators.CONTENT_ON_CARD)
        amount_of_cards_with_content = len(content_on_card)
        print("Amount of cards with content " + str(amount_of_cards_with_content))
        i = 0
        list_of_content = []
        for element in content_on_card:
            new_content = element.text
            list_of_content.append(new_content)
            print("Content # " + str(i) + "\n" + new_content)
            i = i + 1
        list_of_content_set = set(list_of_content)
        print("Total " + str(len(list_of_content)) + " contents, " + str(len(list_of_content_set)) + " of which are unique")
        assert len(list_of_content) == len(list_of_content_set), 'Duplicate content'

    def cards_have_different_links(self):
        link_on_card = self.browser.find_elements(*MainPageLocators.LINK_ON_CARD)
        amount_of_cards_with_link = len(link_on_card)
        print("Amount of cards with link " + str(amount_of_cards_with_link))
        i = 0
        list_of_links = []
        for element in link_on_card:
            new_link = element.get_attribute("href")
            list_of_links.append(new_link)
            print("Link # " + str(i) + "\n" + new_link)
            i = i + 1 
        list_of_links_set = set(list_of_links)
        print("Total " + str(len(list_of_links)) + " links, " + str(len(list_of_links_set)) + " of which are unique")
        assert len(list_of_links) == len(list_of_links_set), 'Links do not lead to internal pages'

    def link_leads_to_the_direction_page(self):
        menu_item = self.browser.find_element(*MainPageLocators.MENU_ITEMS)
        menu_item.click()
        assert "departure" in self.browser.current_url, "The link does not lead to the direction page"

    def link_leads_to_tour_page(self):
        card_link = self.browser.find_element(*MainPageLocators.LINK_ON_CARD)
        card_link.click()
        assert "tour" in self.browser.current_url, "The link does not lead to the tour page"


=======

class MainPage(BasePage):
    def should_be_main_page_link_on_logo(self):
        button = self.browser.find_element(*MainPageLocators.LOGO_LINK)
        button.click()
        heading_main = self.is_element_present(*MainPageLocators.HEADING_MAIN)
        assert heading_main, 'Does not go to the main page when clicking on the logo'

    def should_be_menu_on_page(self):
        menu_main = self.is_element_present(*MainPageLocators.MENU_ON_PAGE)
        assert menu_main, 'Menu is not on the page'

    def should_be_cards_on_page(self):
        cards = self.browser.find_elements(*MainPageLocators.CARDS)
        amount_cards = len(cards)
        print("Amount of cards per page " + str(amount_cards))
        assert amount_cards >= 3, 'Less than three cards per page'

    def links_lead_to_different_pages(self):
        menu_items = self.browser.find_elements(*MainPageLocators.MENU_ITEMS)
        amount_of_menu_items = len(menu_items)
        print("Amount of menu items " + str(amount_of_menu_items))
        i = 0
        list_of_links = []
        for element in menu_items:
            new_link = element.get_attribute("href")
            list_of_links.append(new_link)
            print("Link # " + str(i) + "\n" + new_link)
            i = i + 1
        list_of_links_set = set(list_of_links)
        print("Total " + str(len(list_of_links)) + " links, " + str(len(list_of_links_set)) + " of which are unique")
        assert len(list_of_links) == len(list_of_links_set), 'Duplicate links'            

    def cards_have_different_pictures(self):
        picture_on_card = self.browser.find_elements(*MainPageLocators.PICTURE_ON_CARD)
        amount_of_cards_with_picture = len(picture_on_card)
        print("Amount of cards with pictures " + str(amount_of_cards_with_picture))
        i = 0
        list_of_pictures = []
        for element in picture_on_card:
            new_picture = element.get_attribute("src")
            print("Picture # " + str(i) + "\n" + new_picture)
            list_of_pictures.append(new_picture)
            i = i + 1
        list_of_pictures_set = set(list_of_pictures)
        print("Total " + str(len(list_of_pictures)) + " pictures, " + str(len(list_of_pictures_set)) + " of which are unique")
        assert len(list_of_pictures) == len(list_of_pictures_set), 'Duplicate pictures'

    def cards_have_different_content(self):
        content_on_card = self.browser.find_elements(*MainPageLocators.CONTENT_ON_CARD)
        amount_of_cards_with_content = len(content_on_card)
        print("Amount of cards with content " + str(amount_of_cards_with_content))
        i = 0
        list_of_content = []
        for element in content_on_card:
            new_content = element.text
            list_of_content.append(new_content)
            print("Content # " + str(i) + "\n" + new_content)
            i = i + 1
<<<<<<< HEAD
        list_of_content_set = set(list_of_content)
        print("Total " + str(len(list_of_content)) + " contents, " + str(len(list_of_content_set)) + " of which are unique")
        assert len(list_of_content) == len(list_of_content_set), 'Duplicate content'
=======
>>>>>>> 41354bff3cb46a93de8bddaa6eea90390f7ce909

    def cards_have_different_links(self):
        link_on_card = self.browser.find_elements(*MainPageLocators.LINK_ON_CARD)
        amount_of_cards_with_link = len(link_on_card)
        print("Amount of cards with link " + str(amount_of_cards_with_link))
        i = 0
        list_of_links = []
        for element in link_on_card:
            new_link = element.get_attribute("href")
            list_of_links.append(new_link)
            print("Link # " + str(i) + "\n" + new_link)
<<<<<<< HEAD
            i = i + 1 
        list_of_links_set = set(list_of_links)
        print("Total " + str(len(list_of_links)) + " links, " + str(len(list_of_links_set)) + " of which are unique")
        assert len(list_of_links) == len(list_of_links_set), 'Links do not lead to internal pages'

    def link_leads_to_the_direction_page(self):
        menu_item = self.browser.find_element(*MainPageLocators.MENU_ITEMS)
        menu_item.click()
        assert "departure" in self.browser.current_url, "The link does not lead to the direction page"
=======
            i = i + 1
>>>>>>> 41354bff3cb46a93de8bddaa6eea90390f7ce909

    def link_leads_to_tour_page(self):
        card_link = self.browser.find_element(*MainPageLocators.LINK_ON_CARD)
        card_link.click()
        assert "tour" in self.browser.current_url, "The link does not lead to the tour page"


<<<<<<< HEAD
=======
#
#    def __init__(self, *args, **kwargs):
#        super(MainPage, self).__init__(*args, **kwargs)
>>>>>>> d42005df3da7e08d61e91e312fb2f442b5ef2fa0
>>>>>>> 41354bff3cb46a93de8bddaa6eea90390f7ce909
