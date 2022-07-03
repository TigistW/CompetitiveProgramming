# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        values = []
        while head:
          values.append(head.val)
          head = head.next
        size = len(values)
        decimal = 0
        for i in range(size):
          decimal += (2 ** i) * values[size - i - 1]
        return decimal
          
          
        
      
      
      