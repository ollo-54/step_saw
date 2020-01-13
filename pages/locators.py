from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGO_LINK = (By.CLASS_NAME, 'navbar-brand')
    HEADING_MAIN = (By.CLASS_NAME, 'display-4')
    MENU_ON_PAGE = (By.CLASS_NAME, 'navbar-expand-lg')
    CARDS = (By.CLASS_NAME, 'mb-3')
    MENU_ITEMS = (By.CLASS_NAME, 'nav-link')
    PICTURE_ON_CARD = (By.CLASS_NAME, 'card-img-top')
    CONTENT_ON_CARD = (By.CLASS_NAME, 'card-text')
    LINK_ON_CARD = (By.CLASS_NAME, 'btn-primary')

class DeparturePageLocators():
    DEPARTURE_HEADER = (By.CLASS_NAME, 'display-5')
    CARDS_IN_DESCRIPTION = (By.CLASS_NAME, 'mb-4')
    
class TourPageLocators():
    TOUR_HEADER = (By.CLASS_NAME, 'btn-success')
    PRICE_TOUR = (By.CLASS_NAME, 'btn-lg')


