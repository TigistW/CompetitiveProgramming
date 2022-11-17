# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        def inorder(node):
          if node:
            inorder(node.left)
            ans.append(node.val)
            inorder(node.right)
            
        inorder(root)
        count = Counter(ans)
        mode = 0
        for i in count:
          mode = max(mode, count[i])
        res = []  
        for i in count:
          if count[i] == mode:
            res.append(i)
        return res
          
            
        