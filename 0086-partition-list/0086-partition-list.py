# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        one = less = ListNode(0)
        two = more = ListNode(0)
        
        while head:
          if head.val < x:
            less.next = head
            less = less.next
          else:
            more.next = head
            more = more.next
          head = head.next
        
        less.next = None
        more.next = None
        
        two = two.next
        less.next = two
        return one.next
        
          