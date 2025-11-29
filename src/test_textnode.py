import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_url(self):
        node = TextNode("We're testing the url", TextType.ITALIC, "https://boots.dev")
        node2 = TextNode("We're testing the url", TextType.ITALIC, None)
        self.assertNotEqual(node, node2)

    def test_invalid_enum_attribute_raises(self):
        with self.assertRaises(AttributeError):
            _ = TextType.SQUIGGLES  # no such member

    def test_invalid_enum_value_raises(self):
        with self.assertRaises(ValueError):
            _ = TextType("squiggles")


if __name__ == "__main__":
    unittest.main()