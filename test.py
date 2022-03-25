# Definition for a binary tree node.
class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


class Solution:
  def mergeTrees(self, root1, root2):

    if not (root1 and root2):
      return root1 or root2

    queue1, queue2 = [root1], [root2]

    while queue1 and queue2:
      node1, node2 = queue1.pop(0), queue2.pop(0)

      if node1 and node2:
        node1.val = node1.val + node2.val

        if (not node1.left) and node2.left:
            node1.left = TreeNode(0)

        if (not node1.right) and node2.right:
            node1.right = TreeNode(0)
        queue1.append(node1.left)
        queue1.append(node1.right)
        queue2.append(node2.left)
        queue2.append(node2.right)
        
    return root1


# DRIVER CODE
tree1node1 = TreeNode(1)
tree1node3 = TreeNode(3)
tree1node2 = TreeNode(2)
tree1node5 = TreeNode(5)

tree2node2 = TreeNode(2)
tree2node1 = TreeNode(1)
tree2node3 = TreeNode(3)
tree2node4 = TreeNode(4)
tree2node7 = TreeNode(7)

root1 = tree1node1
tree1node1.left = tree1node3
tree1node1.right = tree1node2
tree1node3.left = tree1node5

root2 = tree2node2
tree2node2.left = tree2node1
tree2node2.right = tree2node3
tree2node1.right = tree2node4
tree2node3.right = tree2node7


solution = Solution()
solution.mergeTrees(root1, root2)