import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
  def test_eq(self):
    node = HTMLNode("div", "This is a div", ["Hello", "World!"])
    node2 = HTMLNode("div", "This is a div", ["Hello", "World!"])
    self.assertEqual(node, node2)

  def test_props(self):
    node = HTMLNode("div", "This is a div", [], {"class": "container"})
    self.assertEqual(node.props_to_html(), " class='container'")

  def test_repr(self):
    node = HTMLNode("div", "This is a div", ["Hello", "World!"], {"class": "container"})
    self.assertEqual(str(node), "HTMLNode(div, This is a div, ['Hello', 'World!'], class='container')")

  def test_html(self):
    node = HTMLNode("div", "This is a div", ["Hello", "World!"], {"class": "container"})
    self.assertEqual(node.to_html(), "<div class='container'>This is a div Hello World!</div>")