# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class TreeNode:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BST:

    def __init__(self):
        self.root = None

    def swap(self, first, second):
        data = first.val
        first.val = second.val
        second.val = data

    def insert(self, node, data):
        if self.root is None:
            self.root = TreeNode(data)
        else:
            if node.val < data:
                if node.right is None:
                    node.right = TreeNode(data)
                else:
                    self.insert(node.right, data)
            else:
                if node.left is None:
                    node.left = TreeNode(data)
                else:
                    self.insert(node.left, data)

    def inorder_traversal(self, node):
        if node is not None:
            self.inorder_traversal(node.left)
            print(node.val)
            self.inorder_traversal(node.right)
        return None

    def inorder_successor(self, node):
        if node.left is None:
            return node
        return self.inorder_successor(node.left)

    def delete(self, node, item):
        if node is None:
            return node

        if item < node.val:
            node.left = self.delete(node.left, item)

        elif item > node.val:
            node.right = self.delete(node.right, item)

        else:
            if node.left is None and node.right is None:
                return None

            elif node.left is None and node.right is not None:
                return node.right

            elif node.left is not None and node.right is None:
                return node.left

            else:
                successor = self.inorder_successor(node.right)
                node.val = successor.val
                node.right = self.delete(node.right, successor.val)

        return node

    def inordertraversal(self, root: TreeNode, array = None):
        if array is None:
            array = []
            
        if root is not None:
            self.inordertraversal(root.left, array)
            array.append(root.val)
            self.inordertraversal(root.right, array)
            return sorted(array)
        else:
            return None
        
    def isValidBST(self, root: TreeNode, array = None, validity = None) -> bool:
        if array is None:
            array = self.inordertraversal(root)

        if validity == False:
            return validity
            
        if root is not None:
            self.isValidBST(root.left, array)
            if array[0] != root.val:
                validity = False
            else:
                validity = True
            array.pop(0)
            self.isValidBST(root.right, array)
        else:
            return None
    


bst = BST()
bst.insert(bst.root, 5)
bst.insert(bst.root, 3)
bst.insert(bst.root, 8)
bst.insert(bst.root, 2)
bst.insert(bst.root, 4)
bst.insert(bst.root, 6)
bst.insert(bst.root, 10)

# node_3 = TreeNode(3)
# node_1 = TreeNode(1)
# node_4 = TreeNode(4)
# node_2 = TreeNode(2)

# node_3.left = node_1
# node_3.right = node_4
# node_4.left = node_2

# bst = BST()
# bst.root = node_3
# Swap 2 nodes to incorrect spots
# bst.swap(bst.root, bst.root.right.left)

bst.inorder_traversal(bst.root)
bst.isValidBST(bst.root)