class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def __repr__(self):
        return f'HTMLNode: {self.tag}, {self.value}, {self.children}, {self.props}'

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if not isinstance(self.props, dict) and self.props is not None:
            raise TypeError('props should be of type dict or None')

        if self.props is None or (isinstance(self.props, dict) and len(self.props) == 0):
            return ''

        html_props = []
        for key, val in self.props.items():
            if val is not None:
                html_props.append(f'{key}="{val}"')

        return f' {" ".join(html_props)}'
