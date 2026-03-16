import unittest
from generatepage import extract_title, generate_page

class TestTitleExtract(unittest.TestCase):
    def test_eq(self):
        title = extract_title("# Hello")
        self.assertEqual("Hello", title)
    def test_eq2(self):
        title = extract_title("#    Hello  ")
        self.assertEqual("Hello", title)

if __name__ == "__main__":
    unittest.main()
