"""
This module provides functions for working with Click scenario
"""


from base_page import BasePage
from selenium.webdriver.common.by import By


class SearchLocators():
    BUTTON_TO_CLICK = (By.CLASS_NAME, 'btn-primary')
    SUCCESS_BUTTON = (By.CLASS_NAME, 'btn-success')


class BadButtonHelper(BasePage):

    def bad_button_click(self):
        return self.find_element(SearchLocators.BUTTON_TO_CLICK, time=2).click()

    def good_button_appears(self):
        return bool(len(self.find_elements(SearchLocators.SUCCESS_BUTTON, time=2)))
