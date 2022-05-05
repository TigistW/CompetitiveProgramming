# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
  def insertionSortList(self, head: ListNode) -> ListNode:
    node = ListNode(0)
    curr = head
    while curr:
      prev = node
      while prev.next and prev.next.val < curr.val:
        prev = prev.next
      next = curr.next
      curr.next = prev.next
      prev.next = curr
      curr = next

    return node.next
            
        