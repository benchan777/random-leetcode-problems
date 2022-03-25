class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

node1 = Node(8)
node2 = Node(3)
node3 = Node(10)
node4 = Node(1)
node5 = Node(6)
node6 = Node(14)

root = node1
node1.left = node2
node1.right = node3
node2.left = node4
node2.right = node5
node3.right = node6

def insert(node, new_node):
    if node == None:
        return Node(data)

    else:
        if new_node.data < node.data:
            if node.left == None:
                node.left = new_node
            else:
                return insert(node.left, new_node)

        if new_node.data > node.data:
            if node.right == None:
                node.right = new_node
            else:
                return insert(node.right, new_node)

def search(node, target):
    if node == None:
        return None
    if node.data == target:
        return 'Found'
    if target < node.data:
        return search(node.left, target)
    if target > node.data:
        return search(node.right, target)

def min_key(node):
    if node != None:
        min_key(node.left)
    return node

def delete(node, target):
    if node == None:
        return node
    if target < node.data:
        node.left = delete(node.left, target)
    elif target > node.data:
        node.right = delete(node.right, target)
    else:
        # Delete node that has no children (leaf node)
        if node.left == None and node.right == None:
            return None

        # Delete node that has one child on the right    
        elif node.left == None and node.right != None:
            return node.right

        # Delete node that has one child on the left
        elif node.right == None and node.left != None:
            return node.left
        
        # Delete node with two children
        else:
            # Find inorder successor to current node
            successor = min_key(node.right)
            node.data = successor.data
            node.right = delete(node.right, successor.data)
            # node.right = successor.right

    return node

def in_order_traversal(node):
    if node != None:
        in_order_traversal(node.left)
        print(node.data)
        in_order_traversal(node.right)
    return None

def pre_order_traversal(node):
    if node != None:
        print(node.data)
        pre_order_traversal(node.left)
        pre_order_traversal(node.right)
    return None

def post_order_traversal(node):
    if node != None:
        post_order_traversal(node.left)
        post_order_traversal(node.right)
        print(node.data)
    return None


insert(root, Node(4))
insert(root, Node(7))
insert(root, Node(13))

# print(search(root, 13))

in_order_traversal(root)
# pre_order_traversal(root)
# post_order_traversal(root)
delete(root, 8)
print("----------------------")
in_order_traversal(root)