# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(node, maxx):
          if not node:
            return
          if node.val >= maxx:
            count[0] += 1
            maxx = node.val
            
          if node.left:
            dfs(node.left,maxx)
          if node.right:
            dfs(node.right,maxx)

          return count[0]

        if not root:
          return 0
        count = [0]
        dfs(root,root.val)
        return count[0]
      
        
          