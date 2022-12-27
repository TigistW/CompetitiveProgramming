# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        B_nodes = set()
        while headB is not None:
          B_nodes.add(headB)
          headB = headB.next
        
        while headA:
          if headA in B_nodes:
            return headA
          headA = headA.next
        return None