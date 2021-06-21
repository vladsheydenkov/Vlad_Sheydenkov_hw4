import unittest
from scenarios.pages.hiddel_layers_page import HiddenHelper
from selenium.common.exceptions import ElementClickInterceptedException


class TestImpossibleSecondClick(unittest.TestCase):
    def setUp(self) -> None:
        self.url = "http://uitestingplayground.com/hiddenlayers"

    def test_impossible_second_click(self):
        page = HiddenHelper(self.url)
        page.go_to_site()
        page.click_on_the_green_button()
        with self.assertRaises(ElementClickInterceptedException):
            page.click_on_the_green_button()
        page.quit()



if __name__ == '__main__':
    unittest.main()
