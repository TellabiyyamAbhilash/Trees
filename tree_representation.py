class node:
    def __init__(self, data=None):
        self.left = None
        self.data = data
        self.right = None

class head:
    def __init__(self, root=None):
        self.root = root

# this insertion works as:
# the new node will be the child for the given parent node. left child after right insertion.
def insert(root, data, parent):
    if parent is None:
        n = node(data)
        root.address = n
        return n
    if parent.left is None:
        n = node(data)
        parent.left = n
        return n
    if parent.right is None:
        n = node(data)
        parent.right = n
        return n

# printing the nodes in level order traersal
def print_nodes(root):
    start = root
    que = []
    if not start:
        return
    que = [start]
    while que:
        node = que.pop(0)
        print(node.data)
        if node.left:
            que.append(node.left)
        if node.right:
            que.append(node.right)

root = node(1)
head = head(root) # can be used for the head pointer of the tree 
insert(root, 2, root)
insert(root, 3, root)

print_nodes(root)
