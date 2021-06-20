"""
This module provides functions for working with Dynamic Table scenario
"""


from base_page import BasePage
from selenium.webdriver.common.by import By


class SearchLocators():
    ROWS = (By.CSS_SELECTOR, '[role="row"]')
    CPU = (By.CLASS_NAME, 'bg-warning')


class DynamicTableHelper(BasePage):

    def find_chrome_cpu(self):
        rows = self.find_elements(SearchLocators.ROWS, time=2)
        for row in rows:
            data_from_row = row.text.split()
            if data_from_row[0] == 'Chrome':
                chrome_cpu = data_from_row[1]
                return f'Chrome CPU: {chrome_cpu}'

    def find_answer_cpu(self):
        return self.find_element(SearchLocators.CPU, time=2).text
