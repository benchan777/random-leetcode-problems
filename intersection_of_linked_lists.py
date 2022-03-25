# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        current_nodeA = headA
        current_nodeB = headB
        
        lenA = 0
        lenB = 0
        
        while current_nodeA != None:
            lenA += 1
            current_nodeA = current_nodeA.next
            
        while current_nodeB != None:
            lenB += 1
            current_nodeB = current_nodeB.next
            
        difference = abs(lenA - lenB)
        current_nodeA = headA
        current_nodeB = headB
        
        if lenA > lenB:
            while difference != 0:
                difference -= 1
                current_nodeA = current_nodeA.next
        if lenB > lenA:
            while difference != 0:
                difference -= 1
                current_nodeB = current_nodeB.next
                
        while current_nodeA != None and current_nodeB != None:
            if current_nodeA == current_nodeB:
                return current_nodeA
            else:
                current_nodeA = current_nodeA.next
                current_nodeB = current_nodeB.next
                
        return None
        
        
#         current_nodeA = headA
#         current_nodeB = headB
                
#         dictA = {}
        
#         while current_nodeA != None:
#             dictA[current_nodeA] = 0
#             current_nodeA = current_nodeA.next
            
#         while current_nodeB != None:
#             if current_nodeB in dictA:
#                 return current_nodeB
#             else:
#                 current_nodeB = current_nodeB.next
                
#         return None
        
        
        
        
#         current_nodeA = headA
#         current_nodeB = headB
        
#         intersection_value = None
        
#         stackA = []
#         stackB = []
        
#         while current_nodeA != None:
#             stackA.insert(0, current_nodeA)
#             current_nodeA = current_nodeA.next
            
#         while current_nodeB != None:
#             stackB.insert(0, current_nodeB)
#             current_nodeB = current_nodeB.next
            
#         while stackA[0] == stackB[0]:
#             intersection_value = stackA.pop(0)
#             stackB.pop(0)
            
#             if len(stackA) == 0 or len(stackB) == 0:
#                 return intersection_value
            
#         return intersection_value
        