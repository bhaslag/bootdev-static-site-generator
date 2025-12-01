class HTMLNode:
  def __init__(self, tag=None, value=None, children=None, props=None):
    self.tag = tag
    self.value = value
    self.children = children
    self.props = props

  def to_html(self):
    raise NotImplementedError("Subclasses must implement this method")
  
  def props_to_html(self):
    if self.props is None:
      return ""
    props_html = " " + " ".join([f"{key}={value}" for key, value in self.props.items()])
    return props_html
  
  def __repr__(self):
    return "HTMLNode({TAG}, {VALUE}, {CHILDREN}, {PROPS})".format(
      TAG = self.tag,
      VALUE = self.value,
      CHILDREN = self.children,
      PROPS = self.props_to_html()
    )