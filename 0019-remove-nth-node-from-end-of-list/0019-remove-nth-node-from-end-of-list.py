# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        first = ListNode(0, head)
        dummy = second = ListNode(0, head)
        
        for i in range(n + 1):
          first = first.next
          
        while first is not None:
              first = first.next
              second = second.next
        else:
          second.next = second.next.next
        return dummy.next
          
          
          
          
            