"""
This module provides functions for working with progress bar scenario
"""


from scenarios.base_page import BasePage
from selenium.webdriver.common.by import By


class SearchLocators():
    PROGRESS_BAR = (By.CSS_SELECTOR, '[aria-valuenow="75"]')
    START_BUTTON = (By.ID, 'startButton')
    STOP_BUTTON = (By.ID, 'stopButton')


class ProgressHelper(BasePage):

    def click_start_button(self):
        self.find_element(SearchLocators.START_BUTTON, time=30).click()

    def click_stop_button(self):
        self.find_element(SearchLocators.STOP_BUTTON, time=30).click()

    def find_progress(self):
        try:
            return self.find_element(SearchLocators.PROGRESS_BAR, time=30)
        except Exception as er:
            print(er)
        return False
