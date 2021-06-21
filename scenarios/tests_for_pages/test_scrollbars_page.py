import unittest
from scenarios.pages.scrollbars_page import ScrollbarHelper


class TestScrollbarsPage(unittest.TestCase):
    def setUp(self) -> None:
        self.url = 'http://uitestingplayground.com/scrollbars'

    def test_scrollbars_page(self):
        page = ScrollbarHelper(self.url)
        page.go_to_site()
        assert page.click_on_hiding_button()
        page.quit()


if __name__ == '__main__':
    unittest.main()
