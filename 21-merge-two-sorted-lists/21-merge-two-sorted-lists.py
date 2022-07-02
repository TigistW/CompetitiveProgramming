# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head=ListNode()
        temp=head
        if list1==None:
            return list2
        if list2==None:
            return list1
        
        while(list1 and list2):
            if list1.val>list2.val:
                temp.next=list2
                # print(list2.val)
                list2=list2.next
            else:
                temp.next=list1
                # print(list1.val)
                list1=list1.next
            temp=temp.next
        temp.next=list1 or list2
        return head.next