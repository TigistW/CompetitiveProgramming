# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        tree = []
        seen = set()
        rt = TreeNode()
        
        def inorder(node):
          if node:
            inorder(node.left)
            tree.append(node)
            inorder(node.right)
          
        inorder(root)
        val = root_one = TreeNode()
        
        for i in range(len(tree)):
          root_one.right = TreeNode(tree[i].val)
          root_one = root_one.right
        return val.right
          