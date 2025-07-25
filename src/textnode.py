from enum import Enum

class TextType(Enum):
    TEXT = "plain_text"
    BOLD = "**bold**"
    ITALIC = "_italic_"
    CODE = "`code`"
    LINK = "[anchor text](url)"
    IMAGES = "![alt text](url)"

class TextNode:
    def __init__(self, text_type: TextType, text: str, url: str = None):
        self.text_type = text_type
        self.content = text
        self.url = url

    def __eq__(self, other):
        if not isinstance(other, TextNode):
            return False
        return (self.text_type == other.text_type and
                self.content == other.content and
                self.url == other.url)
    
    def __repr__(self):
        return f"TextNode({self.text_type}, {self.content}, {self.url})"
    
    def render(self) -> str:
        if self.text_type == TextType.TEXT:
            return self.content
        elif self.text_type == TextType.BOLD:
            return f"**{self.content}**"
        elif self.text_type == TextType.ITALIC:
            return f"_{self.content}_"
        elif self.text_type == TextType.CODE:
            return f"`{self.content}`"
        elif self.text_type == TextType.LINK:
            return f"[{self.content.split('](')[0]}]({self.content.split('](')[1]})"
        elif self.text_type == TextType.IMAGES:
            return f"![{self.content.split('](')[0]}]({self.content.split('](')[1]})"
        else:
            raise ValueError("Unsupported text type")