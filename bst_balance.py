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

    def preorder_traversal(self, node):
        if node is not None:
            print(node.val)
            self.preorder_traversal(node.left)
            self.preorder_traversal(node.right)
        return None

    def createArray(self, root: TreeNode, array = None):
        if array is None:
            array = []
        if root is not None:
            self.createArray(root.left, array)
            array.append(root)
            self.createArray(root.right, array)
            return array
        else:
            return None

    def buildBST(self, start_index, end_index, array):
        if start_index > end_index:
            return None

        else:
            midIndex = (start_index + end_index) // 2
            root = array[midIndex]
            root.left = self.buildBST(start_index, midIndex - 1, array)
            root.right = self.buildBST(midIndex + 1, end_index, array)
        return root

    def balanceBST(self, root, array = None):
        if array is None:
            array = self.createArray(root)

        return self.buildBST(0, len(array) - 1, array)

bst = BST()

node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)

node1.right = node2
node2.right = node3
node3.right = node4
bst.root = node1

# print(bst.createArray(bst.root))
bst.preorder_traversal(bst.root)
bst.balanceBST(bst.root)
print('---------------')
bst.preorder_traversal(bst.root)
