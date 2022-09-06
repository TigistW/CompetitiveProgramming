# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pruneTree(self, node):
      if not node:
        return None

      node.left =  self.pruneTree(node.left)
      node.right = self.pruneTree(node.right)

      if node.left or node.right or node.val == 1:
        return node
      else:
        return None

