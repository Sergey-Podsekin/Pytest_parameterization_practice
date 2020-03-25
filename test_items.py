import time
link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


def test_add_to_cart_button_is_present(browser):
    browser.get(link)
    assert len(browser.find_elements_by_css_selector
        ("[class='btn btn-lg btn-primary btn-add-to-basket']")) \
        != 0, 'No cart button'
    time.sleep(30)


