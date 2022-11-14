"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        def dfs(node):
          if node is None:
            return 0
          elif node.children == []:
            return 1
          else:
            heights = [dfs(child) for child in node.children]
            return max(heights) + 1
          
        return dfs(root)
              
              