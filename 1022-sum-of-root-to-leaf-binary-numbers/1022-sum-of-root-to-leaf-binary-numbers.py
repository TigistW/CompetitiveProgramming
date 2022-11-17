# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        ans = [0]
        def dfs(node, path, total):
          if not node.left and not node.right:
            total += int(path + str(node.val),2)
            ans[0] += total
          else:
            if node.left:
              dfs(node.left, path + str(node.val), total)
            if node.right:
              dfs(node.right, path + str(node.val), total)
          return total
        dfs(root, "", 0)
        return ans[0]
      
            
          