# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        ans = []
        def inorder(node):
          if node:
            inorder(node.left)
            ans.append(node.val)
            inorder(node.right)
        inorder(root)

        left = 0
        right = left + 1
        min_val = math.inf
        while right < len(ans):
          min_val = min(ans[right] -  ans[left], min_val)
          left += 1
          right += 1
        return min_val
          
          
            