# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        ans = []
        def dfs(root, targetSum, path) -> None:
          if root is None:
            return
          if root.val == targetSum and root.left is None and root.right is None:
            ans.append(path + [root.val])
            return

          dfs(root.left, targetSum - root.val, path + [root.val])
          dfs(root.right, targetSum - root.val, path + [root.val])
    
        dfs(root, targetSum, [])
        return ans