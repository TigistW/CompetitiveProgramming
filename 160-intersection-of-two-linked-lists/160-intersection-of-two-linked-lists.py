# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        first = headA
        second = headB

        while first != second:
          if first:
            first = first.next
          else:
            first = headB
            
          if second:
            second = second.next
          else:
            second = headA
          
        return first