
link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"


def test_is_button_present(browser):
    browser.get(link)
    assert browser.find_element_by_css_selector(".btn-add-to-basket"), "No such button"





