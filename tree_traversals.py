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

def pre_order_traversal(root):
    if root:
        print(root.data)
        pre_order_traversal(root.left)
        pre_order_traversal(root.right)

def in_order_traversal(root):
    if root:
        in_order_traversal(root.left)
        print(root.data)
        in_order_traversal(root.right)
    
def post_order_traversal(root):
    if root:
        post_order_traversal(root.left)
        post_order_traversal(root.right)
        print(root.data)

root = node(1)
head = head(root) # can be used for the head pointer of the tree 
b = insert(root, 2, root)
c = insert(root, 3, root)
d = insert(root, 4, b)
e = insert(root, 5, b)
f = insert(root, 6, c)
g = insert(root, 7, c)
h = insert(root, 8, d)
i = insert(root, 9, d)
print("Level Order traversal")
print_nodes(root)
print("Pre Order traversal")
pre_order_traversal(root)
print("In Order traveraal")
in_order_traversal(root)
print("Post order traversal")
post_order_traversal(root)
