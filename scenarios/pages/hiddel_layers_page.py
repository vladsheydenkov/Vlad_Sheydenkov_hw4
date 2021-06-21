"""
This module provides functions for working with Hidden Layers scenario
"""


from scenarios.base_page import BasePage
from selenium.webdriver.common.by import By


class SearchLocators():
    LOCATOR_GREEN_BUTTON = (By.ID, 'greenButton')


class HiddenHelper(BasePage):

    def click_on_the_green_button(self):
        return self.find_element(SearchLocators.LOCATOR_GREEN_BUTTON, time=2).click()
