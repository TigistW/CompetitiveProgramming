# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        temp = head
        ans = temp
        count, counter = 0, 0
        while node:
          count += 1
          node = node.next
        if count == 1:
          return None
        elif count == 2:
          temp.next = None
          return temp
        while temp: 
          if counter == (count // 2):
            temp.val = temp.next.val
            temp.next = temp.next.next
          else:
            temp = temp.next
          counter += 1
        return ans
          
          