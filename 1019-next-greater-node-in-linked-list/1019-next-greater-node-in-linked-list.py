# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        result = []
        #Changing to a stack
        while head:
            result.append(head.val)
            head = head.next
            
        stack = []
        # print(result)
        for i in range(len(result)):
            if not stack:
                stack.append(i)
                # print(stack)
            else:
                while stack and result[stack[-1]] < result[i]:
                    result[stack.pop()] = result[i]
                stack.append(i)
        # print(result)
        # print(stack)
        while stack:
            result[stack.pop()] = 0 
        return result