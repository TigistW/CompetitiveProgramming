# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.ans = None
        def backtrack(node):
          if not node:
            return False
          
          from_left = backtrack(node.left)
          from_right = backtrack(node.right)
          
          if p == node or q == node:
            mid = True
          else:
            mid = False
            
          if from_left + from_right + mid >= 2: 
            self.ans = node
          
          return mid or from_left or from_right
          
        backtrack(root)
        return self.ans
          
          