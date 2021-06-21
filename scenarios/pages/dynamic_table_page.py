"""
This module provides functions for working with Dynamic Table scenario
"""


from scenarios.base_page import BasePage
from selenium.webdriver.common.by import By


class SearchLocators():
    ROWS = (By.CSS_SELECTOR, '[role="row"]')
    CPU = (By.CLASS_NAME, 'bg-warning')


def find_cpu(list_with_elements):
    for element in list_with_elements[1:]:
        if '%' in element:
            return f'Chrome CPU: {element}'


class DynamicTableHelper(BasePage):

    def find_chrome_cpu(self):
        rows = self.find_elements(SearchLocators.ROWS, time=2)
        for row in rows:
            data_from_row = row.text.split()
            if data_from_row[0] == 'Chrome':
                return find_cpu(data_from_row)

    def find_answer_cpu(self):
        return self.find_element(SearchLocators.CPU, time=2).text
