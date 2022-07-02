# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:

        headone = ListNode(0,head)
        # print(cur)
        cur = headone
        while head:
          if head.val != val:
            cur.next = head
            cur = cur.next
            head = head.next
          else:
            head = head.next
            
        cur.next = None
        return headone.next
        
            
            

            
            
          
            
            
            
            
        