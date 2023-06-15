# code for tranforming the complete binary tree
# which is in linked list representation (class in python)
# to a max heap


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
            return

        queue = [self.root]

        while queue:
            current = queue.pop(0)

            if current.left is None:
                current.left = Node(data)
                return
            else:
                queue.append(current.left)

            if current.right is None:
                current.right = Node(data)
                return
            else:
                queue.append(current.right)


    def print_nodes(self):
        start = self.root
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
                
def inter_nodes(root,i_nodes):
    que = [root]
    while que:
        node = que.pop(0)
        if node.left or node.right:
            i_nodes.append(node)
        if node.left:
            que.append(node.left)
        if node.right:
            que.append(node.right)
    return i_nodes

def heapify(start_node):
    large = start_node.data
    left = start_node.left
    right = start_node.right
    
    if left and right:
        if left.data > right.data and left.data > large:
            temp = start_node.data
            start_node.data = start_node.left.data
            start_node.left.data = temp
            heapify(start_node.left)
            return
        elif right.data > left.data and right.data > large:
            temp = start_node.data
            start_node.data = start_node.right.data
            start_node.right.data = temp
            heapify(start_node.right)
            return
        else:
            return
    
    if left:
        if left.data > large:
            temp = start_node.data
            start_node.data = start_node.left.data
            start_node.left.data = temp
            heapify(start_node.left)
            return
    if right:
        if right.data > large:
            temp = start_node.data
            start_node.data = start_node.right.data
            start_node.right.data = temp
            heapify(start_node.right)
            return

def build_heap(i_nodes):
    for i in range(len(i_nodes)-1,-1,-1):
        heapify(i_nodes[i])
    return 
    
# Usage example
tree = BinaryTree()

tree.insert(10)
tree.insert(14)
tree.insert(19)
tree.insert(26)
tree.insert(27)
tree.insert(31)
tree.insert(33)
tree.insert(35)
tree.insert(42)
tree.insert(44)

tree.print_nodes()
i_nodes  = inter_nodes(tree.root,[])
build_heap(i_nodes)
print("after heaping")
tree.print_nodes()





