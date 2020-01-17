from pages.main_page import MainPage
from pages.departure_page import DeparturePage
from pages.tour_page import TourPage

def test_should_be_departure_header(browser, link):
    link_dep=f'{link}/departure/msk'
    page = DeparturePage(browser, link_dep)
    page.open()
    header_text = page.get_header_text()
    expected_text = "Летим Из Москвы"
    page.should_be_exact_text(expected_text, header_text)

def test_amount_tour_cards_on_departure_page(browser, link):
    link_dep=f'{link}/departure/msk'
    page = DeparturePage(browser, link_dep)
    page.open()
    tour_cards_amount = page.get_amount_of_tour_cards()
    assert tour_cards_amount >= 3, f"Expected 3+ tours tour card, but got {tours_amount}"

def test_departure_general_info(browser, link):
    link_dep=f'{link}/departure/msk'
    page = DeparturePage(browser, link_dep)
    page.open()
    departure_description_text = page.get_departure_description_text()
    tour_cards_amount = page.get_amount_of_tour_cards()
    assert tour_cards_amount >= 3, f"Expected 3+ tours tour card, but got {tours_amount}"
    
    amount_expected_text =  f"Найдено {tour_cards_amount} туров"
    page.should_be_exact_text(amount_expected_text, departure_description_text)
    
    price_expected_text = 'от 52000 до 68000 и'
    page.should_be_exact_text(price_expected_text, departure_description_text)
    
    days_expected_text = 'от 8 ночей до 10 ночей'
    page.should_be_exact_text(days_expected_text, departure_description_text)

def test_tour_cards_on_departure_page_have_different_pictures(browser, link):
    link_dep=f'{link}/departure/msk'
    page = DeparturePage(browser, link_dep)
    page.open()
    page.tour_cards_have_different_pictures()

def test_tour_cards_on_departure_page_have_different_content(browser, link):
    link_dep=f'{link}/departure/msk'
    page = DeparturePage(browser, link_dep)
    page.open()
    page.tour_cards_have_different_content()

def test_tour_cards_on_departure_page_have_different_link(browser, link):
    link_dep=f'{link}/departure/msk'
    page = DeparturePage(browser, link_dep)
    page.open()
    page.tour_cards_have_different_links()

def test_tour_cards_link_on_departure_leads_to_tour_page(browser, link):
    link_dep=f'{link}/departure/msk'
    page = DeparturePage(browser, link_dep)
    page.open()
    page.click_on_the_tour_cards_link()
    page_tour = TourPage(browser, link)
    page_tour.should_be_tour_page()

