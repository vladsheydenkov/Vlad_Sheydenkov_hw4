"""
This module provides functions for working with Scrollbars scenario
"""


from base_page import BasePage
from selenium.webdriver.common.by import By


class SearchLocators():
    HIDING_BUTTON = (By.ID, 'hidingButton')


class ScrollbarHelper(BasePage):

    def click_on_hiding_button(self):
        try:
            self.find_element(SearchLocators.HIDING_BUTTON, time=2).click()
            return True
        except Exception as er:
            print(er)
            return False
