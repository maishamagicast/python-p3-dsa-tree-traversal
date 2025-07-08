class Tree:
  def __init__(self, root = None):
    self.root = root

  def get_element_by_id(self, id):
    nodes_to_visit=[self.root]
    while nodes_to_visit:
      node=nodes_to_visit.pop()
      if node['id']==id:
        return node
      nodes_to_visit.extend(node.get('children', []))
    return None
      
# {
#   'tag_name': 'h1',
#   'id': 'heading',
#   'text_content': 'Title',
#   'children': []
# }