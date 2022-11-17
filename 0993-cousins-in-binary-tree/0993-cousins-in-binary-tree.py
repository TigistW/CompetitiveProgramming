# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        
        x_par, x_dep = [0], [0]
        y_par , y_dep = [0], [0]
        
        def dfs(node, parent, depth):
          if node:
            if node.val == x:
              x_par[0] = parent.val
              x_dep[0] = depth
            if node.val == y:
              y_par[0] = parent.val
              y_dep[0] = depth
              
            if node.left:
              dfs(node.left, node, depth + 1)
            if node.right:
              dfs(node.right, node, depth + 1)
        dfs(root, root, 0)
        # print(x_par, y_par, x_dep, y_dep)
        if x_par != y_par and x_dep == y_dep:
          return True
        return False
        
              
              
              