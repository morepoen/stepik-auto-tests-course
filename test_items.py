import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_is_button_present(browser):
    browser.get(link)
    add_to_basket_button = len(browser.find_elements_by_css_selector(".btn-add-to-basket"))
    assert add_to_basket_button > 0, "Button add-to-basket does not exist"









