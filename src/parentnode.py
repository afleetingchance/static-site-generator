from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError('ParentNode needs a tag')
        if not isinstance(self.tag, str):
            raise TypeError('ParentNode tag needs to be a string')
        if self.children is None or (isinstance(self.children, list) and len(self.children) == 0):
            raise ValueError('ParentNode needs children')
        if not isinstance(self.children, list):
            raise TypeError('ParentNode children needs to be a list')
        
        children_html = ''
        for child in self.children:
            children_html += child.to_html()

        return f'<{self.tag}>{children_html}</{self.tag}>'