import unittest
from scenarios.pages.verify_tex_page import VerifyHelper


class TestVerifyText(unittest.TestCase):
    def setUp(self) -> None:
        self.url = 'http://uitestingplayground.com/verifytext'

    def test_verify_text(self):
        page = VerifyHelper(self.url)
        page.go_to_site()
        unstable_text = page.find_text()
        self.assertEqual(unstable_text.text, 'Welcome UserName!')
        page.quit()


if __name__ == '__main__':
    unittest.main()
