class HTMLNode():
    def __init__(self, tag: str=None, value :str=None, children: list=None, props: dict=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("error: to_html not implemented")
    
    def props_to_html(self):
        if not self.props:
            return ""
        string = ""
        for key in self.props:
            string += f' {key}="{self.props[key]}"'
        return string + " "
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children} {self.props})"
    
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)
    
    def to_html(self):
        if self.value is None:
            raise ValueError("error: leaf node value is none")
        if self.tag is None:
            return self.value
        if self.props:
            return f"<{self.tag}{self.props_to_html().rstrip()}>{self.value}</{self.tag}>"
        return f"<{self.tag}>{self.value}</{self.tag}>"
    
    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"
    
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props = None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("error: parent node has no tag")
        if self.children is None:
            raise ValueError("error: parent node has no children")
        opening_tag = f"<{self.tag}{self.props_to_html()}>"
        closing_tag = f"</{self.tag}>"
        content = ""
        for child in self.children:
            content = content + child.to_html()
        return f"{opening_tag}{content}{closing_tag}"
    