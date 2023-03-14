# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        ans = []
        def dfs(node, path):

            if not node.left and not node.right:
                path.append(str(node.val))
                ans.append("".join(path.copy()))
                return
            path.append(str(node.val))
            if node.left:
                dfs(node.left, path)
                path.pop()
            if node.right:
                dfs(node.right, path)
                path.pop()
            
        dfs(root, [])
        print(ans)
        summ = 0
        for i in ans:
            summ += int(i)
        return summ
        
        
            