# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        head = ListNode(0,head)
        if head.next == None:
          return False
        
        slow, fast = head.next, head.next.next
        while True:
          
          if slow == fast:
            return True
          if fast == None or fast.next == None: 
            return False
          
          slow = slow.next
          fast = fast.next.next      