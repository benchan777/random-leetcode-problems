class Node:
    def __init__(self, info):
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

def preOrder(root):
    if root == None:
        return
    print (root.info, end=" ")
    preOrder(root.left)
    preOrder(root.right)
    
class BinarySearchTree:
    def __init__(self): 
        self.root = None

#Node is defined as
#self.left (the left child of the node)
#self.right (the right child of the node)
#self.info (the value of the node)

    def insert(self, val):
        #Enter you code here.
        if self.root == None:
            self.root =  Node(val)
        else:
            return self.insert_helper(self.root, val)
        
    def insert_helper(self, node, val):
        if node is None:
            node = Node(val)
        elif val < node.info:
            node.left = self.insert_helper(node.left, val)
        else:
            node.right = self.insert_helper(node.right, val)
        return node
        

tree = BinarySearchTree()
t = [4, 2, 3, 1, 7, 6]

# arr = list(map(int, input().split()))

for i in range(len(t)):
    tree.insert(t[i])

preOrder(tree.root)
