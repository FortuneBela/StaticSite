class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        all_attributes = ""
        
        if self.props is None:
            return ""
        
        for key, value in self.props.items():
            all_attributes += f' {key}="{value}"'

        return all_attributes
        
    def __repr__(self):
        return f"tag={self.tag}, value={self.value}, children={self.children}, props={self.props}"
    
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)
    
    def to_html(self):
        if self.value is None:
            raise ValueError
        elif self.tag is None:
            return self.value
        else:
            properties = self.props_to_html()
            opening = f"<{self.tag}{properties}>"
            closing = f"</{self.tag}>"
            return f"{opening}{self.value}{closing}"
        
    def __repr__(self):
        return f"tag={self.tag}, value={self.value}, props={self.props}"
    
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)
    
    def to_html(self):
        final_string = ""
        if self.tag is None:
            raise ValueError("Missing tag arugment")
        elif self.children is None:
            raise ValueError("Missing children argument")
        else:
            for child in self.children:
                final_string += child.to_html()
            return f"<{self.tag}{self.props_to_html()}>{final_string}</{self.tag}>"