"""
This module provides pytest fixture
"""


import pytest
from webdriver_manager.firefox import GeckoDriverManager
from selenium import webdriver


@pytest.fixture(scope="session")
def browser():
    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    yield driver
    driver.quit()
