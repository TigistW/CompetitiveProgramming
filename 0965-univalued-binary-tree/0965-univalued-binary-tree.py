# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        val = root.val
        diff = [False]
        def dfs(node):
          if node:
            if node.val != val:
              diff[0] = True
            if node.left:
              dfs(node.left)
              
            if node.right:
              dfs(node.right)
              
        dfs(root)
        if diff[0]:
          return False
        return True