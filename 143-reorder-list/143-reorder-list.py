# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    def reorderList(self, head: ListNode) -> None:
        if not head or not head.next or not head.next.next:
            return
        
        slow=head
        fast=head
     
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            
            
        headsec = slow.next
        slow.next = None
        
        nodd= ListNode(0, None)
        
        while headsec:
            tmp = headsec.next
            headsec.next = nodd.next
            nodd.next = headsec
            headsec = tmp
        headone = head
        headsec = nodd.next
        while headone and headsec:
            tmp = headsec
            headsec = headsec.next
            tmp.next = headone.next
            headone.next = tmp
            headone = headone.next.next