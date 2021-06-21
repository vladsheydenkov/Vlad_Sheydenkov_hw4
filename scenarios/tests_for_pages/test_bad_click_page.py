import unittest
from scenarios.pages.bad_click_page import BadButtonHelper


class TestBadClick(unittest.TestCase):
    def setUp(self) -> None:
        self.url = 'http://uitestingplayground.com/click'

    def test_bad_click(self):
        page = BadButtonHelper(self.url)
        page.go_to_site()
        page.bad_button_click()
        self.assertTrue(page.good_button_appears())
        page.quit()


if __name__ == '__main__':
    unittest.main()
