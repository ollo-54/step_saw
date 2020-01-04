from .pages.main_page import MainPage

link = "https://stepik-flask01.herokuapp.com/"

def est_menu_on_Page(browser):
    browser.get(link)
    menu = browser.find_element_by_css_selector("[class='navbar navbar-expand-lg navbar-light bg-light']")
    assert menu, "not is menu"

def est_logo_link(browser):
    browser.get(link)
    button = browser.find_element_by_css_selector("[class='navbar-brand']")
    button.click()
    head_main = browser.find_element_by_css_selector("[class='display-4']")
    assert head_main, 'Menu is not on the page'

def est_amount_cards(browser):
    browser.get(link)
    cards = browser.find_elements_by_css_selector("[class='card mb-3']")
    amount_cards = len(cards)
    print("Amount of cards per page " + str(amount_cards))
    assert amount_cards >= 3, 'Less than three cards per page'

def est_links_lead_to_different_pages(browser):
    browser.get(link)
    menu_items = browser.find_elements_by_css_selector("[class='nav-link']")
    amount_of_menu_items = len(menu_items)
    print("Amount of menu items " + str(amount_of_menu_items))
    i = 0
    for element in menu_items:
#        print(i)
#        print(menu_items)
        new_link = element.get_attribute("href")
#        print(new_link)
#        menu_items.click()
#        new_link = browser.window_handles[i]
        assert link != new_link, 'Duplicate links'
        print("Link # " + str(i) + "\n" + new_link)
        i = i + 1
#        new_link.close()

def est_cards_have_different_pictures(browser):
    browser.get(link)
    picture_on_card = browser.find_elements_by_css_selector("[class='card-img-top img-fluid']")
#    print(picture_on_card)
    picture = " "
    amount_of_cards_with_picture = len(picture_on_card)
    print("Amount of cards with pictures " + str(amount_of_cards_with_picture))
    i = 0
    for element in picture_on_card:
#        print(i)
#        print(menu_items)
        picture_new = element.get_attribute("src")
#        print(picture_new)
#        menu_items.click()
#        new_link = browser.window_handles[i]
        assert picture != picture_new, 'Duplicate pictures'
        print("Picture # " + str(i) + "\n" + picture_new)
        i = i + 1

def est_cards_have_different_content(browser):
    browser.get(link)
    content_on_card = browser.find_elements_by_css_selector("[class='card-text']")
#    print(content_on_card)
    content = " "
    amount_of_cards_with_content = len(content_on_card)
    print("Amount of cards with content " + str(amount_of_cards_with_content))
    i = 0
    for element in content_on_card:
#        print(i)
#        print(menu_items)
        content_new = element.text
#        print(picture_new)
#        menu_items.click()
#        new_link = browser.window_handles[i]
        assert content != content_new, 'Duplicate content'
        print("Content # " + str(i) + "\n" + content_new)
        i = i + 1    

def test_cards_have_different_link(browser):
    browser.get(link)
    link_on_card = browser.find_elements_by_css_selector("[class='btn btn-sm btn-primary']")
#    print(content_on_card)
    link_one = " "
    amount_of_cards_with_link = len(link_on_card)
    print("Amount of cards with link " + str(amount_of_cards_with_link))
    i = 0
#    link1 = ("https://stepik-flask01.herokuapp.com/tour/6")
    for element in link_on_card:
#        print(i)
#        print(menu_items)
        link_new = element.get_attribute("href")
#        print(picture_new)
#        menu_items.click()
#        new_link = browser.window_handles[i]
        assert link != link_new and link_one != link_new, 'Links do not lead to internal pages'
        print("Link # " + str(i) + "\n" + link_new)
        i = i + 1    

        

'''@pytest.mark.login_guest
class TestLoginFromMainPage():
    def test_guest_can_go_to_login_page(self, test_browser):

        page = MainPage(test_browser, link) 
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(test_browser, test_browser.current_url)
        login_page.should_be_login_page()

    def test_guest_should_see_login_link(self, test_browser):

        page = MainPage(test_browser, link)
        page.open()
        page.should_be_login_link()

def test_guest_cant_see_product_in_basket_opened_from_main_page(test_browser):
    page = MainPage(test_browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(test_browser, test_browser.current_url)
    basket_page.should_be_basket_link()
    basket_page.should_be_empty_basket()
    basket_page.should_be_message_empty()
'''
