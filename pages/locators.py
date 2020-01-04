from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGO_LINK = (By.CLASS_NAME, "navbar-brand") #knopka logo
    HEADING_MAIN = (By.CLASS_NAME, "display-4") #glavnaya ctr
    MENU_ON_PAGE = (By.CLASS_NAME, "navbar-expand-lg")  #menu
    AMOUNT_CARDS = (By.CLASS_NAME, "mb-3")
    AMOUNT_OF_MENU_ITEMS = (By.CLASS_NAME, "nav-link")
    PICTURE_ON_CARD = (By.CLASS_NAME, "card-img-top")
    CONTENT_ON_CARD = (By.CLASS_NAME, "card-text")
    LINK_ON_CARD = (By.CLASS_NAME, "btn-primary")


