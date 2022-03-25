def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
  ans = []
  reverse = False
  
  if root == None:
    return
  
  queue = [root]
  
  while queue:
    temp = []
    length = len(queue)
    
    while length > 0:
      if reverse == True: #reverse order, pop from end of the queue
        node = queue.pop()
        temp.append(node.val)
      else: #forward order, pop from the front of the queue
        node = queue.pop(0)
        temp.append(node.val) 

      if reverse == True: #insert new nodes from the front of the queue to avoid interfering with popping from the end
        if node.right is not None:
          queue.insert(0, node.right)
        if node.left is not None:
          queue.insert(0, node.left)
      else: #insert new nodes to the end of the queue to avoid interfering with popping from the front of the queue
        if node.left is not None:
          queue.append(node.left)
        if node.right is not None:
          queue.append(node.right)
          
      length -= 1
                            
    if reverse == True:
      reverse = False
    else:
      reverse = True
    
    ans.append(temp)
    
  return ans