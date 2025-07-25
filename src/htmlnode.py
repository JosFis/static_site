class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        #An HTMLNode without a tag will just render as raw text
        #An HTMLNode without a value will be assumed to have children
        #An HTMLNode without children will be assumed to have a value
        #An HTMLNode without props simply won't have any attributes

        self.tag = tag
        self.value = value
        self.children = children if children is not None else []
        self.props = props if props is not None else {}

    def to_html(self):
        '''
        if self.tag is None:
            return self.value or ""
        props_str = " ".join(f'{key}="{value}"' for key, value in self.props.items())
        children_str = "".join(child.to_html() for child in self.children)
        return f"<{self.tag} {props_str}>{self.value or ''}{children_str}</{self.tag}>"
        '''
        raise NotImplementedError("to_html method is not implemented yet")
    
    def props_to_html(self):
        return " ".join(f'{key}="{value}"' for key, value in self.props.items())
    
    def __repr__(self):
        return f"HTMLNode(tag={self.tag}, value={self.value}, children={self.children}, props={self.props})"
        
class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None):
        super().__init__(tag=tag, value=value, children=[], props=props)

    def to_html(self):
        if self.value is None:
            raise ValueError("LeafNode must have a value to render")
        if self.tag is None:
            return self.value
        props_str = self.props_to_html()
        return f"<{self.tag}{props_str}>{self.value}</{self.tag}>"