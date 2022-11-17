# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        if not root:
          return []
        def preOrder(node):
          if node:
            ans.append(node.val)
            preOrder(node.left)
            preOrder(node.right)
        preOrder(root)
        return ans
        