import unittest
from scenarios.pages.ajax_data_page import WaitForAjaxHelper


class TestAjaxWait(unittest.TestCase):
    def setUp(self) -> None:
        self.url = 'http://uitestingplayground.com/ajax'

    def test_ajax_wait(self):
        page = WaitForAjaxHelper(self.url)
        page.go_to_site()
        page.click_on_the_ajax_button()
        text = page.wait_until_text_is_appeared()
        self.assertEqual(text, 'Data loaded with AJAX get request.')
        page.quit()


if __name__ == '__main__':
    unittest.main()
