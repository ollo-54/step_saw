from .pages.main_page import MainPage

link = "https://stepik-flask01.herokuapp.com/"
    
def test_logo_link_should_be_presented(browser):
    page = MainPage(browser, link)
    page.open()
    page.should_be_main_page_link_on_logo()

def test_menu_should_be_presented(browser):
    page = MainPage(browser, link)
    page.open()
    page.should_be_menu_on_page()

def test_amount_cards_on_page(browser):
    page = MainPage(browser, link)
    page.open()
    page.should_be_cards_on_page()

def test_links_lead_to_different_pages(browser):
    page = MainPage(browser, link)
    page.open()
    page.links_lead_to_different_pages()

def test_cards_have_different_pictures(browser):
    page = MainPage(browser, link)
    page.open()
    page.cards_have_different_pictures()

def test_cards_have_different_content(browser):
    page = MainPage(browser, link)
    page.open()
    page.cards_have_different_content()

def test_cards_have_different_link(browser):
    page = MainPage(browser, link)
    page.open()
    page.cards_have_different_links()

def test_link_leads_to_the_direction_page(browser):
    page = MainPage(browser, link)
    page.open()
    page.link_leads_to_the_direction_page()

def test_link_leads_to_tour_page(browser):
    page = MainPage(browser, link)
    page.open()
    page.link_leads_to_tour_page()

