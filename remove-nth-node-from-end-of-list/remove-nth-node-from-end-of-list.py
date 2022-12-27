# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        count = 0
        temp = head
        while temp is not None:
          count += 1
          temp = temp.next
          
        val, target, temp2 = 1, count - n, head
          
        if target == 0:
          head = head.next
          return head
        else:
          while head:
            if val == target:
              head.next = head.next.next
            val += 1
            head = head.next
          return temp2

            
          
          
        