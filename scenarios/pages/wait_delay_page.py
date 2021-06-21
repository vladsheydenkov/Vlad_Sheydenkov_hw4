"""
This module provides functions for working with Load Delay scenario
"""


from base_page import BasePage
from selenium.webdriver.common.by import By


class SearchLocators():
    LOCATOR_APPEARED_BUTTON = (By.CLASS_NAME, 'btn')


class WaitHelper(BasePage):

    def click_on_the_appeared_button(self):
        try:
            self.find_element(SearchLocators.LOCATOR_APPEARED_BUTTON, time=2).click()
            return True
        except Exception as er:
            print(er)
            return False
