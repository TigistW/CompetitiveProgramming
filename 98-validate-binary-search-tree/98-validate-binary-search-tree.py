# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def isValidBST(root,minNode, maxNode):
          if not root:
            return True
          if minNode and root.val <= minNode.val:
            return False
          if maxNode and root.val >= maxNode.val:
            return False

          return isValidBST(root.left, minNode, root) and \
              isValidBST(root.right, root, maxNode)

        return isValidBST(root, None, None)