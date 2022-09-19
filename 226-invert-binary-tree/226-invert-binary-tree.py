# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def invert(node):
          if not node:
            return None
          else:
            node.left, node.right = node.right,node.left
            
            invert(node.left)
            invert(node.right)
          
        node = root
        invert(node)
        return node