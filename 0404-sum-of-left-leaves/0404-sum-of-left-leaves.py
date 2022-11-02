# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        summ = [0]
        
        def dfs(node,is_left):
          if not node.left and not node.right and is_left:
              summ[0] += node.val
          
          if node.left:
            dfs(node.left, True)
          if node.right:
            dfs(node.right, False)
            
          return summ[0]
        
        if not root:
          return 0
        return dfs(root, False)