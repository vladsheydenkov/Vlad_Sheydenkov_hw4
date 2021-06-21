import unittest
from scenarios.pages.progress_bar_page import ProgressHelper


class TestProgressBar(unittest.TestCase):
    def setUp(self) -> None:
        self.url = 'http://uitestingplayground.com/progressbar'

    def test_progress_bar(self):
        page = ProgressHelper(self.url)
        page.go_to_site()
        page.click_start_button()
        progress = page.find_progress()
        page.click_stop_button()
        answer = progress.get_attribute('aria-valuenow')
        self.assertEqual(answer, '75')
        page.quit()


if __name__ == '__main__':
    unittest.main()
