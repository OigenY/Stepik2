link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_guest_should_see_basket_button(browser):
    browser.implicitly_wait(10)
    browser.get(link)
    browser.find_element_by_css_selector("[class='add-to-basket']")
    #time.sleep(10)
def test_element_present(browser):
    browser.implicitly_wait(10)
    browser.get(link)
    option = browser.find_element_by_css_selector("[class='add-to-basket']")
    assert option is not None, "Element not found"