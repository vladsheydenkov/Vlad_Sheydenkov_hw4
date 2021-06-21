import unittest
from scenarios.pages.dynamic_table_page import DynamicTableHelper


class TestDynamicTable(unittest.TestCase):
    def setUp(self) -> None:
        self.url = 'http://uitestingplayground.com/dynamictable'

    def test_dynamic_table(self):
        page = DynamicTableHelper(self.url)
        page.go_to_site()
        chrome_cpu = page.find_chrome_cpu()
        answer_cpu = page.find_answer_cpu()
        self.assertEqual(chrome_cpu, answer_cpu)
        page.quit()


if __name__ == '__main__':
    unittest.main()
