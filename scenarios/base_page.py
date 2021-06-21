"""
This module provides functions for searching web elements
"""


from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.firefox import GeckoDriverManager
from selenium import webdriver


class BasePage():

    def __init__(self, url):
        self.browser = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        self.url = url

    def find_element(self, locator, time=10):
        return WebDriverWait(self.browser, time).until(EC.presence_of_element_located(locator),
                                                       message=f"Can't find element by locator {locator}")

    def find_elements(self, locator, time=10):
        return WebDriverWait(self.browser, time).until(EC.presence_of_all_elements_located(locator),
                                                       message=f"Can't find elements by locator {locator}")

    def go_to_site(self):
        return self.browser.get(self.url)

    def quit(self):
        self.browser.quit()

