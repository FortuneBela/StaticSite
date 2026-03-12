import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):

    def test_prop_none(self):
        node = HTMLNode("tag", "this would be a value", None, None)
        self.assertEqual(node.props_to_html(), "")
    
    def test_multi(self):
        node = HTMLNode("tag", "value", None, {"href": "https://www.boot.dev", "target": "_blank"})
        self.assertEqual(node.props_to_html(), ' href="https://www.boot.dev" target="_blank"')

    def test_repr(self):
        node = HTMLNode("tag", "this would be a value", None, None)
        self.assertEqual(node.__repr__(), "tag=tag, value=this would be a value, children=None, props=None")

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_tagless(self):
        node = LeafNode(None, "this should return")
        self.assertEqual(node.to_html(), "this should return")

    def test_to_html_no_value(self):
        node = LeafNode("p", None)
        with self.assertRaises(ValueError):
            node.to_html()

    def test_leaf_properties(self):
        node = LeafNode("p", "Hello, world!", {"href": "https://www.boot.dev"} )
        self.assertEqual(node.to_html(), '<p href="https://www.boot.dev">Hello, world!</p>')

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
    )

    def test_no_child(self):
        node = ParentNode("div", None)
        with self.assertRaises(ValueError):
            node.to_html()

    def test_no_child(self):
        node = ParentNode("div", [])
        self.assertEqual(node.to_html(), "<div></div>")

        

if __name__ == "__main__":
    unittest.main()