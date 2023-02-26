# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        summ = [0]
        def findSum(node):
            if node:
                findSum(node.left)
                summ[0] += node.val
                findSum(node.right)
        def traverse(node):
            if node:
                traverse(node.left)
                summ[0] -= node.val
                node.val += summ[0]
                traverse(node.right)
        findSum(root) 
        traverse(root)
        return root
        
        
                
            