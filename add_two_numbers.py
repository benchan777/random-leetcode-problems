# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        newNode = ListNode()
        newHead = newNode
        carry = 0
        
        while l1 is not None or l2 is not None:
            if l1 is not None:
                value1 = l1.val
            else:
                value1 = 0
                
            if l2 is not None:
                value2 = l2.val
            else:
                value2 = 0
                
            summation = value1 + value2 + carry
            
            if summation > 9:
                summation -= 10
                carry = 1
            else:
                carry = 0
                
            newNode.next = ListNode(summation)
            newNode = newNode.next
            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next
            
        if carry > 0:
            newNode.next = ListNode(carry)
        
        return newHead.next