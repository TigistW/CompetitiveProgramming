# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        arr= []
        def recur(node):
          if node:
            recur(node.left)
            arr.append(node.val)
            recur(node.right)
            
        recur(root)
        return arr
          
        