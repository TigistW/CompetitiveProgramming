# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp=head
        count=0
        while temp:
            count+=1
            temp=temp.next
        if count==1:
            return None
        delNode=count-n
        temp=head
        if delNode==0:
            head=temp.next
            return head
        while delNode>1:
            temp=temp.next
            delNode-=1
        if temp.next:
            temp.next=temp.next.next
        return head