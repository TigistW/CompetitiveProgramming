# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        current = head  
        while fast and fast.next:
            current = slow
            slow = slow.next
            fast = fast.next.next
        current.next = None
        reversedList = self.revList(slow)
        current = head
        while current:
            if current.val != reversedList.val:
                return False
            current = current.next 
            reversedList = reversedList.next   
        return True 
    def revList(self,head):    
        previous = None
        node = head
        while node:
            nextNode = node.next
            node.next = previous
            previous = node
            node = nextNode
            
            # print(node,".......",nextNode,".......",previous,)
            
        # print(previous)
        return previous