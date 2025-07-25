from textnode import TextNode, TextType

print("hello world")

def main():
    # The function should create a new TextNode object with some dummy values. Print the object, and make sure it looks like you'd expect. For example, my code printed:
    # TextNode(This is some anchor text, link, https://www.boot.dev)

    node = TextNode(TextType.LINK, "This is some anchor text", "https://www.boot.dev")
    print(node)
    print(TextNode(TextType.PLAIN, "This is a plain text node", ""))
    print(TextNode(TextType.BOLD, "This is a bold text node", ""))
    print(TextNode(TextType.ITALIC, "This is an italic text node", ""))
    print(TextNode(TextType.CODE, "This is a code text node", ""))

main()