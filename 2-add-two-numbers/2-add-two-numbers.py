# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        head.val = (l1.val + l2.val) % 10
        rem = (l1.val + l2.val) // 10
        # print(head,rem)
        l1, l2 = l1.next, l2.next
        temp = head
        while (l1 != None or l2 != None) or rem > 0:
            resNode = ListNode()
            if l1 != None:
                resNode.val += l1.val
                l1 = l1.next
            if l2 != None:
                resNode.val += l2.val
                l2 = l2.next  
            resNode.val += rem
            rem = (resNode.val) // 10
            resNode.val = resNode.val % 10
            temp.next = resNode
            temp = resNode
        temp.next = None
        return head