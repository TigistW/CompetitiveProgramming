# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        second=head
        first=head
        while(second.next and second.next.next):
            first=first.next
            second=second.next.next
            
        if second.next:
            first=first.next
            
        return first
            