"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        dic = {None : None}
        
        curr = head
        while curr:
            dup = Node(curr.val)
            dic[curr] = dup
            curr = curr.next
            
        curr = head
        while curr:
            dup = dic[curr]
            dup.next = dic[curr.next]
            dup.random = dic[curr.random]
            curr = curr.next
        return dic[head]