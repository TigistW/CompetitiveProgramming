# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getCycle(self, head):
        if head.next == None:
          return None
        
        slow, fast = head.next, head.next.next
        while True:
          if slow == fast:
            return fast
          if fast == None or fast.next == None: 
            return None
          
          slow = slow.next
          fast = fast.next.next
          
    def detectCycle(self, head: Optional[ListNode]) -> bool:
        head = ListNode(0,head)
        cycle_point = self.getCycle(head)
        
        if cycle_point == None:
          return None
        else:
          one = head
          two = cycle_point


          while one != two:
            one, two = one.next, two.next
          else:
            return one

        