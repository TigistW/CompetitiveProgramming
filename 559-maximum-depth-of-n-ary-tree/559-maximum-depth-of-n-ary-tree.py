"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, node: 'Node') -> int:
        if not node:
            return 0
        if not node.children:
            return 1
        return max(self.maxDepth(child) for child in node.children) + 1
        
        
    