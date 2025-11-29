from textnode import TextNode
from textnode import TextType

def main():
    new_node = TextNode('fake content text', TextType.IMAGE, 'https://boot.dev')
    print(new_node)

main()