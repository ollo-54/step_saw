from pages.main_page import MainPage
from pages.departure_page import DeparturePage
from pages.tour_page import TourPage

def test_should_be_departure_header(browser, link):       # вариант c проверкой в base_page.py
    link_dep=f'{link}/departure/msk'
    page = DeparturePage(browser, link_dep)
    page.open()
    departure_header = page.get_header()
    page.should_be_departure_header(departure_header)

def test_amount_cards_on_departure_page(browser, link):
    link_dep=f'{link}/departure/msk'
    page = DeparturePage(browser, link_dep)
    page.open()
    page.get_amount_of_tour_cards()

def test_departure_general_info(browser, link):      # объеденены количество и цены
    link_dep=f'{link}/departure/msk'
    page = DeparturePage(browser, link_dep)
    page.open()
    departure_description = page.get_description()
    tours_amount = page.get_amount_of_tour_cards()
    page.should_be_cards_in_description(departure_description, tours_amount)
    page.should_be_price_in_description(departure_description)

def test_days_in_description(browser, link):      # это тот, которого нет в ТЗ, можно вложить в general_info
    link_dep=f'{link}/departure/msk'
    page = DeparturePage(browser, link_dep)
    page.open()
    departure_description = page.get_description()
    page.should_be_days_in_description(departure_description)


def test_cards_on_departure_page_have_different_pictures(browser, link):
    link_dep=f'{link}/departure/msk'
    page = DeparturePage(browser, link_dep)
    page.open()
    page.cards_have_different_pictures()

def test_cards_on_departure_page_have_different_content(browser, link):
    link_dep=f'{link}/departure/msk'
    page = DeparturePage(browser, link_dep)
    page.open()
    page.cards_have_different_content()

def test_cards_on_departure_page_have_different_link(browser, link):
    link_dep=f'{link}/departure/msk'
    page = DeparturePage(browser, link_dep)
    page.open()
    page.cards_have_different_links()

def test_card_link_on_departure_leads_to_tour_page(browser, link):    # это тот, который ты добавил
    link_dep=f'{link}/departure/msk'
    page = DeparturePage(browser, link_dep)
    page.open()
    page.click_on_the_tour_link()
    page_tour = TourPage(browser, link)
    page_tour.should_be_tour_page()

