"""
This module provides functions for working with Text Input scenario
"""



from base_page import BasePage
from selenium.webdriver.common.by import By


class SearchLocators():
    INPUT_FIELD = (By.ID, 'newButtonName')
    BUTTON = (By.ID, 'updatingButton')


class TextInputHelper(BasePage):

    def send_keys_to_updating_field(self, key):
        return self.find_element(SearchLocators.INPUT_FIELD, time=2).send_keys(key)

    def click_on_updating_button(self):
        return self.find_element(SearchLocators.BUTTON, time=2).click()

    def get_new_button_name(self):
        return self.find_element(SearchLocators.BUTTON, time=2).text
