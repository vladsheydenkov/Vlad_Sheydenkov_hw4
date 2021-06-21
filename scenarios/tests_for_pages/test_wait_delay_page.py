import unittest
from scenarios.pages.wait_delay_page import WaitHelper


class TestLoadDelay(unittest.TestCase):
    def setUp(self) -> None:
        self.url = 'http://uitestingplayground.com/loaddelay'

    def test_load_delay(self):
        page = WaitHelper(self.url)
        page.go_to_site()
        self.assertTrue(page.click_on_the_appeared_button())
        page.quit()


if __name__ == '__main__':
    unittest.main()
