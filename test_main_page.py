from .pages.main_page import MainPage

link = "https://stepik-flask01.herokuapp.com/"


def test_logo_link(browser):
    page = MainPage(browser, link)
    page.open()
    page.go_to_main_page()


def test_menu_on_Page(browser):
    page = MainPage(browser, link)
    page.open()
    page.menu_on_page()


def test_amount_cards_on_page(browser):
    page = MainPage(browser, link)
    page.open()
    page.amount_cards_on_page()


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
    page.cards_have_different_link(link)
