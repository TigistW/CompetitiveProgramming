# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp=head
        res, count, cur = ListNode(-101), 1, head
        temp = res
        while cur:
            if cur and cur.next and cur.next.val == cur.val:
                count += 1
                cur = cur.next
            else:
                if count == 1:
                    # print(cur.val, count)
                    temp.next = cur
                    temp_next = cur.next
                    cur.next = None
                    temp = temp.next
                    cur = temp_next
                    
                else:
                    count = 1
                    cur = cur.next

                
            

        return res.next
