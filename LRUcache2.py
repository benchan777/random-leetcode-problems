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
    self.head.next = self.tail
    self.tail.prev = self.head

  def get(self, key: int) -> int:
    if key in self.hashmap:
      node = self.hashmap[key]
      self.delete(node)
      self.add(node)
      return node.value
    else:
      return -1

  def put(self, key: int, value: int) -> None:
    newNode = Node(key, value)
    if key in self.hashmap:
      self.delete(self.hashmap[key])

    if self.currentCapacity < self.capacity:
      self.currentCapacity += 1
      self.hashmap[key] = newNode
      self.add(newNode)
    else:
      nodeToDelete = self.head.next
      self.delete(nodeToDelete)
      del self.hashmap[nodeToDelete.key]

      self.hashmap[key] = newNode
      self.add(newNode)

  def add(self, node):
    previous = self.tail.prev
    previous.next = node
    node.prev = previous
    node.next = self.tail
    self.tail.prev = node

  def delete(self, node):
    previous = node.prev
    nextNode = node.next
    previous.next = nextNode
    nextNode.prev = previous

lRUCache = LRUCache(2)
lRUCache.put(1,1)
lRUCache.put(2,2)
lRUCache.get(1)
lRUCache.put(3,3)
lRUCache.get(2)
lRUCache.put(4,4)
lRUCache.get(1)
lRUCache.get(3)
lRUCache.get(4)
