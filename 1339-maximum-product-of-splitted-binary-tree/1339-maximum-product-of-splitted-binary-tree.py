# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        ttl = [0]
        def summ(node):
          if not node:
            return None
          ttl[0] += node.val
          summ(node.left)
          summ(node.right)
          
            
        
        ans = [0]
        def dfs(node):
          if not node:
            return 0
          
          if not node.right and not node.left:
            return node.val
          
          left = dfs(node.left)
          right = dfs(node.right)

          one = left * (ttl[0] - left)
          two = right * (ttl[0] - right)

          ans[0] = max([ans[0],one, two])

          return left + right + node.val
      
        summ(root)
        dfs(root)
        return ans[0] % ((10 ** 9) + 7)
        
            
          
          
          
          
          
          
          
          
          
          
          