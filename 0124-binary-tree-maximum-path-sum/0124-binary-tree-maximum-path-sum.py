# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import sys
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.ans = root.val
        
        def dfs(root):
            if not root:
                return 0
            
            # try to max path in left of curr node, 0 to avoid -ve values
            l = max(0, dfs(root.left))
            # try to max path in right of curr node
            r = max(0, dfs(root.right))
            
            # check if max path goes through curr node
            self.ans = max(self.ans, root.val+l+r)
            
            # return max path either on left or right
            return root.val + max(l,r)
        
        
        dfs(root)
        return self.ans