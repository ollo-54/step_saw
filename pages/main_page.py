from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import MainPageLocators

class MainPage(BasePage):
    def go_to_main_page(self):
        button = self.browser.find_element(*MainPageLocators.LOGO_LINK)
        button.click()
        heading_main = self.is_element_present(*MainPageLocators.HEADING_MAIN)
        assert heading_main, 'Does not go to the main page when clicking on the logo'

    def menu_on_page(self):
        menu_main = self.is_element_present(*MainPageLocators.MENU_ON_PAGE)
        assert menu_main, 'Menu is not on the page'

    def amount_cards_on_page(self):
        cards = self.browser.find_elements(*MainPageLocators.AMOUNT_CARDS)
        amount_cards = len(cards)
        print("Amount of cards per page " + str(amount_cards))
        assert amount_cards >= 3, 'Less than three cards per page'
    
    def links_lead_to_different_pages(self):
        link = "https://stepik-flask01.herokuapp.com/"
        menu_items = self.browser.find_elements(*MainPageLocators.AMOUNT_OF_MENU_ITEMS)
        amount_of_menu_items = len(menu_items)
        print("Amount of menu items " + str(amount_of_menu_items))
        i = 0
        for element in menu_items:
            new_link = element.get_attribute("href")
            assert link != new_link, 'Duplicate links'
            print("Link # " + str(i) + "\n" + new_link)
            i = i + 1

    def cards_have_different_pictures(self):
        picture_on_card = self.browser.find_elements(*MainPageLocators.PICTURE_ON_CARD)
        picture = " "
        amount_of_cards_with_picture = len(picture_on_card)
        print("Amount of cards with pictures " + str(amount_of_cards_with_picture))
        i = 0
        for element in picture_on_card:
            new_picture = element.get_attribute("src")
            assert picture != new_picture, 'Duplicate pictures'
            print("Picture # " + str(i) + "\n" + new_picture)
            i = i + 1

    def cards_have_different_content(self):
        content_on_card = self.browser.find_elements(*MainPageLocators.CONTENT_ON_CARD)
        content = " "
        amount_of_cards_with_content = len(content_on_card)
        print("Amount of cards with content " + str(amount_of_cards_with_content))
        i = 0
        for element in content_on_card:
            new_content = element.text
            assert content != new_content, 'Duplicate content'
            print("Content # " + str(i) + "\n" + new_content)
            i = i + 1 

    def cards_have_different_link(self, link):
        link_on_card = self.browser.find_elements(*MainPageLocators.LINK_ON_CARD)
        link_one = " "
        amount_of_cards_with_link = len(link_on_card)
        print("Amount of cards with link " + str(amount_of_cards_with_link))
        i = 0
        for element in link_on_card:
            new_link = element.get_attribute("href")
            assert link != new_link and link_one != new_link, 'Links do not lead to internal pages'
            print("Link # " + str(i) + "\n" + new_link)
            i = i + 1 



#
#    def __init__(self, *args, **kwargs):
#        super(MainPage, self).__init__(*args, **kwargs)
