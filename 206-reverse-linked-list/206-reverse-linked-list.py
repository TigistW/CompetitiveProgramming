# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        lst = []
        new =  ListNode()
        temp = new
        
        while (head != None):
            lst.append(head.val)
            head = head.next     
        count = len(lst) - 1 
        while (count != -1):
            temp.next = ListNode(lst[count])
            count -= 1
            temp = temp.next      
        return new.next