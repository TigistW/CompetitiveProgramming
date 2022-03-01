# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, node: Optional[TreeNode]) -> int:
        
        self.tilt = 0  
        self.dfs(node)
        return self.tilt
    
    def dfs(self,node):
        if node == None:
            return 0
        sumLeft = self.dfs(node.left)
        sumRight = self.dfs(node.right) 
        
        self.tilt += abs(sumLeft - sumRight)
        return sumLeft + sumRight + node.val
        
        
            