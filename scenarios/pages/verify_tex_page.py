"""
This module provides functions for working with verify text scenario
"""


from scenarios.base_page import BasePage
from selenium.webdriver.common.by import By


class SearchLocators():
    TEXT = (By.XPATH,  '//span[ normalize-space(.)="Welcome UserName!"]')


class VerifyHelper(BasePage):

    def find_text(self):
        return self.find_element(SearchLocators.TEXT, time=30)
