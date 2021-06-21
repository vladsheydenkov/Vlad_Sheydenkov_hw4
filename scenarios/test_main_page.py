"""
Module with tests
"""


import pytest
from pages.hiddel_layers_page import HiddenHelper
from selenium.common.exceptions import ElementClickInterceptedException
from pages.wait_delay_page import WaitHelper
from pages.ajax_data_page import WaitForAjaxHelper
from pages.client_side_delay_page import WaitForDelayHelper
from pages.bad_click_page import BadButtonHelper
from pages.text_input_page import TextInputHelper
from pages.scrollbars_page import ScrollbarHelper
from pages.dynamic_table_page import DynamicTableHelper


def test_impossible_second_click(browser):
    link = "http://uitestingplayground.com/hiddenlayers"
    page = HiddenHelper(browser, link)
    page.go_to_site()
    page.click_on_the_green_button()
    with pytest.raises(ElementClickInterceptedException):
        page.click_on_the_green_button()


def test_load_delay(browser):
    link = 'http://uitestingplayground.com/loaddelay'
    page = WaitHelper(browser, link)
    page.go_to_site()
    assert page.click_on_the_appeared_button()


def test_ajax_wait(browser):
    link = 'http://uitestingplayground.com/ajax'
    page = WaitForAjaxHelper(browser, link)
    page.go_to_site()
    page.click_on_the_ajax_button()
    text = page.wait_until_text_is_appeared()
    assert text == 'Data loaded with AJAX get request.'


def test_client_delay(browser):
    link = 'http://uitestingplayground.com/clientdelay'
    page = WaitForDelayHelper(browser, link)
    page.go_to_site()
    page.click_on_the_ajax_button()
    text = page.wait_until_text_is_appeared()
    assert text == 'Data calculated on the client side.'


def test_bad_click(browser):
    link = 'http://uitestingplayground.com/click'
    page = BadButtonHelper(browser, link)
    page.go_to_site()
    page.bad_button_click()
    assert page.good_button_appears()


def test_button_renaming(browser):
    link = 'http://uitestingplayground.com/textinput'
    new_name = 'updated'
    page = TextInputHelper(browser, link)
    page.go_to_site()
    page.send_keys_to_updating_field(new_name)
    page.click_on_updating_button()
    button_name = page.get_new_button_name()
    assert button_name == new_name


def test_scrollbars_page(browser):
    link = 'http://uitestingplayground.com/scrollbars'
    page = ScrollbarHelper(browser, link)
    page.go_to_site()
    assert page.click_on_hiding_button()


def test_dynamic_table(browser):
    link = 'http://uitestingplayground.com/dynamictable'
    page = DynamicTableHelper(browser, link)
    page.go_to_site()
    chrome_cpu = page.find_chrome_cpu()
    answer_cpu = page.find_answer_cpu()
    assert chrome_cpu == answer_cpu
