import pytest
import time
from selenium.common.exceptions import NoSuchElementException


@pytest.mark.parametrize('book', ["coders-at-work_207"])
def test_add_to_basket_button_is_present(browser, book):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/{book}/"
    browser.get(link)

    time.sleep(10)  # to visually check the language of the page and button
    try:
        assert browser.find_element_by_css_selector(".btn-add-to-basket")
    except NoSuchElementException:
        assert False, 'The button "Add to basket" is missed 0_0'
