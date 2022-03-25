class Node:
  def __init__(self, data):
    self.val = data
    self.left = None
    self.right = None

# node1 = Node(8)
# node2 = Node(3)
# node3 = Node(10)
# node4 = Node(1)
# node5 = Node(6)
# node6 = Node(14)
# node7 = Node(4)
# node8 = Node(7)
# node9 = Node(13)

# root = node1
# node1.left = node2
# node1.right = node3
# node2.left = node4
# node2.right = node5
# node3.right = node6
# node5.left = node7
# node5.right = node8
# node6.left = node9

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)

root = node1
node1.left = node2
# node1.right = node3
# node2.left = node4
# node2.right = node5

def main(root):
  arr = []
  array = in_order_traversal(root, arr)
  sorted_array = sorted(array)
  if array == sorted_array:
    return True
  else:
    return False


def in_order_traversal(node, array):
  if node == None:
    return array

  in_order_traversal(node.left, array)
  array.append(node.val)
  in_order_traversal(node.right, array)
  return array

def diameter(root):
  diameter = 0
  diameter = dfs(root, diameter)
  return diameter

def dfs(node, diameter):
  if node is None:
    return 0

  left = dfs(node.left, diameter)
  right = dfs(node.right, diameter)
  diameter = max(diameter, left + right)

  return max(left, right) + 1
 
# print(main(root))
print(diameter(root))