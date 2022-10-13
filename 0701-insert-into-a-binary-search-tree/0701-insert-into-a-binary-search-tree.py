# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
      def search(node):
        if node.val < val and node.right:
          return search(node.right)
        elif node.val > val and node.left:
            return search(node.left)
        return node
          
      if not root:
        node = TreeNode(0, None, None)
        node.val = val
        return node
      node = search(root)
      if node.val > val: 
        node.left = TreeNode(0, None, None)
        node.left.val = val
      else:
        node.right = TreeNode(0, None, None)
        node.right.val = val
        
      return root
        
        
        