import unittest
from scenarios.pages.text_input_page import TextInputHelper


class TestButtonRenaming(unittest.TestCase):
    def setUp(self) -> None:
        self.url = 'http://uitestingplayground.com/textinput'

    def test_button_renaming(self):
        new_name = 'updated'
        page = TextInputHelper(self.url)
        page.go_to_site()
        page.send_keys_to_updating_field(new_name)
        page.click_on_updating_button()
        button_name = page.get_new_button_name()
        self.assertEqual(button_name, new_name)
        page.quit()


if __name__ == '__main__':
    unittest.main()
