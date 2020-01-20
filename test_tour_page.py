from pages.main_page import MainPage
from pages.departure_page import DeparturePage
from pages.tour_page import TourPage
from data_handler import Data

def test_tour_title_on_departure_page_and_tour_page(browser, link):
    link_dep = f'{link}/departure/msk'
    page = DeparturePage(browser, link_dep)
    page.open()
    departure_tour_title_text = page.get_departure_tour_title_text()
    page.click_on_the_tour_cards_link()
    page = TourPage(browser, link_dep)
    tour_title_text = page.get_tour_title_text()
    assert departure_tour_title_text == tour_title_text, f'The title of the tour on the destination page "{departure_tour_title_text}" does not match the title of the tour on the tour page "{tour_title_text}"'
    
def test_tour_general_info(browser, link):
    link_tour = f'{link}tour/4'
    page = TourPage(browser, link_tour)
    page.open()
    data = Data()
    tour_page_title_text = page.get_tour_description_text()
    
    tour_description_text = f'{data.get_tour_duration_of_stay(id=4)} Ночей'
    page.should_be_exact_text(tour_description_text, tour_page_title_text)
    
    tour_page_title = data.get_departure(departure='msk')
    page.should_be_exact_text(tour_page_title, tour_page_title_text)

def test_tour_price(browser,link):
    link_tour = f'{link}tour/4'
    page = TourPage(browser, link_tour)
    page.open()
    data = Data()
    tour_page_price_text = page.get_tour_price_text()
    tour_page_price = f'за {data.get_tour_price(id=4)}'
    page.should_be_exact_text(tour_page_price, tour_page_price_text)

def test_tours_have_different_pictures_and_content(browser, link):
    page = TourPage(browser, link)
    data = Data()
    tour_picture_1 = data.tour_picture(id=1)
    tour_content_1 = data.tour_content(id=1)

    tour_picture_2 = data.tour_picture(id=2)
    tour_content_2 = data.tour_content(id=2)
    
    assert tour_picture_1 != tour_picture_2, 'Duplicate pictures in tours'
    assert tour_content_1 != tour_content_2, 'Duplicate content in tours'


