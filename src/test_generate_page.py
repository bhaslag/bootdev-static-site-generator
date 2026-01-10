import unittest

from generate_page import extract_markdown_h1

class TestGeneratePage(unittest.TestCase):
        def test_extract_h1(self):
            md = """
# This is a title 




This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
            title = extract_markdown_h1(md)

            self.assertEqual(
                title,
                "This is a title"
            )

if __name__ == "__main__":
    unittest.main()