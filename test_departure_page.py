from pages.main_page import MainPage
from pages.departure_page import DeparturePage
from pages.tour_page import TourPage

#dep = input('Enter departure link ')

def test_should_be_departure_header(browser, link):
#    link_dep=f'{link}/departure/{dep}'
    link_dep=f'{link}/departure/msk'
    page = DeparturePage(browser, link_dep)
    page.open()
    page.should_be_departure_header()

def test_should_be_departure_header1(browser, link):       # вариант 
    link_dep=f'{link}/departure/msk'
    page = DeparturePage(browser, link_dep)
    page.open()
    departure_header = page.get_header()
    page.should_be_departure_header1(departure_header)

# ====================================

def test_cards_in_description(browser, link):     # вариант 1 
    link_dep=f'{link}/departure/msk'
    page = DeparturePage(browser, link_dep)
    page.open()
    departure_description = page.get_description()
    page.should_be_cards_in_description(departure_description)

def test_should_be_cards_in_description2(browser, link):  # вариант 2 с расчётом количества кaрточек
    link_dep=f'{link}/departure/msk'
    page = DeparturePage(browser, link_dep)
    page.open()
    departure_description = page.get_description()
    page.should_be_cards_in_description2(departure_description)

# ====================================

def test_price_in_description(browser, link):
    link_dep=f'{link}/departure/msk'
    page = DeparturePage(browser, link_dep)
    page.open()
    departure_description = page.get_description()
    page.should_be_price_in_description(departure_description)

def test_days_in_description(browser, link):      # это тот, которого нет в ТЗ
    link_dep=f'{link}/departure/msk'
    page = DeparturePage(browser, link_dep)
    page.open()
    departure_description = page.get_description()
    page.should_be_days_in_description(departure_description)

def test_amount_cards_on_departure_page(browser, link):
    link_dep=f'{link}/departure/msk'
    page = MainPage(browser, link_dep)
    page.open()
    page.should_be_cards_on_page()

def test_cards_on_departure_page_have_different_pictures(browser, link):
    link_dep=f'{link}/departure/msk'
    page = MainPage(browser, link_dep)
    page.open()
    page.cards_have_different_pictures()

def test_cards_on_departure_page_have_different_content(browser, link):
    link_dep=f'{link}/departure/msk'
    page = MainPage(browser, link_dep)
    page.open()
    page.cards_have_different_content()

def test_cards_on_departure_page_have_different_link(browser, link):
    link_dep=f'{link}/departure/msk'
    page = MainPage(browser, link_dep)
    page.open()
    page.cards_have_different_links()
