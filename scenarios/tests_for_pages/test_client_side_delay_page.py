import unittest
from scenarios.pages.client_side_delay_page import WaitForDelayHelper


class TestClientDelay(unittest.TestCase):
    def setUp(self) -> None:
        self.url = 'http://uitestingplayground.com/clientdelay'

    def test_client_delay(self):
        page = WaitForDelayHelper(self.url)
        page.go_to_site()
        page.click_on_the_ajax_button()
        text = page.wait_until_text_is_appeared()
        self.assertEqual(text, 'Data calculated on the client side.')
        page.quit()


if __name__ == '__main__':
    unittest.main()
