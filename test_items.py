from selenium.common.exceptions import NoSuchElementException

link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"


def test_is_button_present(browser):

    try:
        browser.get(link)
        browser.find_element_by_css_selector(".btn-add-to-basket")
    except NoSuchElementException:
        return False
    return True
