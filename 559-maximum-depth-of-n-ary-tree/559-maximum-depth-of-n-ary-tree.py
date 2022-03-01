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
        max_depth = 0
        for child in node.children:
            max_depth = max(max_depth, self.maxDepth(child))
        return max_depth + 1
        
        
    