# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        stack = []
        stack.append(cloned)
        while stack:
          node = stack.pop()
          if node.val == target.val:
            return node
          if node.left:
            stack.append(node.left)
          if node.right:
            stack.append(node.right)
            
        