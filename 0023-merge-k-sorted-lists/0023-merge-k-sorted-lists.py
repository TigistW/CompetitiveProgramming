# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap=[]
        a = ans=ListNode(None)
        for list in lists:
            while list:
                heappush(heap,list.val)
                list=list.next
        # print(heap)        
        while heap:
            ans.next=ListNode(heappop(heap))
            ans=ans.next
        # print(ans)
        return a.next