class Node:
  def __init__(self, key, value):
    self.key = key
    self.value = value
    self.next = None
    self.prev = None

class LRUCache:
  def __init__(self, capacity: int):
    self.capacity = capacity
    self.hashmap = {}
    self.head = Node(0,0)
    self.tail = Node(0,0)
    self.currentCapacity = 0

  def get(self, key: int) -> int:
    if key in self.hashmap:
      nodeValue = self.hashmap[key].value
      self.moveNode(key)
      return nodeValue
    else:
      return -1

  def put(self, key: int, value: int) -> None:
    self.addNode(key, value)
    return None

  #head (1,1) (2,2) (3,3) (4,4) tail
  def addNode(self, key, value):
    if key not in self.hashmap and self.currentCapacity == 0:
      newNode = Node(key, value)
      self.head.next = newNode
      self.tail.prev = newNode
      newNode.prev = self.head
      newNode.next = self.tail
      self.hashmap[key] = newNode
      self.currentCapacity += 1
    elif key not in self.hashmap and self.currentCapacity < self.capacity: #still room in LL. Add new node to tail
      newNode = Node(key, value)
      tempTail = self.tail
      tempPrev = self.tail.prev
      tempPrev.next = newNode
      newNode.prev = tempPrev
      newNode.next = tempTail
      tempTail.prev = newNode

      # newNode.prev = self.tail.prev
      # newNode.next = self.tail
      # self.tail.prev = newNode
      self.hashmap[key] = newNode
      self.currentCapacity += 1
    elif key not in self.hashmap and self.currentCapacity == self.capacity: #capacity has been reached. remove oldest node
      newNode = Node(key, value)
      self.hashmap.pop(self.head.next.key)
      self.deleteNode()
      #insert new node between dummy head and dummy head's previous node
      tempTail = self.tail
      tempPrev = self.tail.prev
      tempPrev.next = newNode
      newNode.prev = tempPrev
      newNode.next = tempTail
      tempTail.prev = newNode
      #store new node into hashmap
      self.hashmap[key] = newNode
      # self.currentCapacity -=1
    else: #duplicate key added. replace and move to the tail
      duplicateNode = self.hashmap[key]
      duplicateNodePrev = duplicateNode.prev
      duplicateNodeNext = duplicateNode.next
      duplicateNodePrev.next = duplicateNodeNext
      duplicateNodeNext.prev = duplicateNodePrev

      duplicateNode.value = value
      tempTail = self.tail
      tempPrev = self.tail.prev
      tempPrev.next = duplicateNode
      duplicateNode.prev = tempPrev
      duplicateNode.next = tempTail
      tempTail.prev = duplicateNode

  def deleteNode(self): #delete the least recently used node (head of the LL)
    self.head.next = self.head.next.next
    self.head.next.prev = self.head

  def moveNode(self, key): #move retrieved node to the tail
    currentNode = self.hashmap[key]
    prevNode = currentNode.prev
    nextNode = currentNode.next
    prevNode.next = nextNode
    nextNode.prev = prevNode

    #insert current node between dummy tail & dummy tail's prev
    tempTail = self.tail
    tempPrev = self.tail.prev
    tempPrev.next = currentNode
    currentNode.prev = tempPrev
    currentNode.next = tempTail
    tempTail.prev = currentNode
        
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

  def printLinkedList(self):
    tempArray = []
    tempHead = self.head
    while tempHead is not None:
      tempArray.append([tempHead.key, tempHead.value])
      tempHead = tempHead.next
    print(tempArray)
        
# lRUCache = LRUCache(2);
# lRUCache.put(1, 1); # cache is {1=1}
# lRUCache.printLinkedList()
# lRUCache.put(2, 2); # cache is {1=1, 2=2}
# lRUCache.printLinkedList()
# lRUCache.get(1);    # return 1
# lRUCache.printLinkedList()
# lRUCache.put(3, 3); # LRU key was 2, evicts key 2, cache is {1=1, 3=3}
# lRUCache.printLinkedList()
# lRUCache.get(2);    # returns -1 (not found)
# lRUCache.printLinkedList()
# lRUCache.put(4, 4); # LRU key was 1, evicts key 1, cache is {4=4, 3=3}
# lRUCache.printLinkedList()
# lRUCache.get(1);    # return -1 (not found)
# lRUCache.printLinkedList()
# lRUCache.get(3);    # return 3
# lRUCache.printLinkedList()
# lRUCache.get(4);    # return 4
# lRUCache.printLinkedList()
# lRUCache.put(3, 3)
# lRUCache.printLinkedList()

lRUCache = LRUCache(2)
lRUCache.put(1,0)
lRUCache.put(2,2)
lRUCache.get(1)
lRUCache.put(3,3)
lRUCache.get(2)
lRUCache.put(4,4)
lRUCache.get(1)
lRUCache.get(3)
lRUCache.get(4)
