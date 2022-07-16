# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
      ans = []
      def dfs(root, path):

        if not root.left and not root.right:
          path = "".join(path) + str(root.val)
          ans.append(path)
          return 
        path.append(str(root.val) + "->")
        if root.left:
          dfs(root.left,path)
        if root.right:
          dfs(root.right,path)
        path.pop()
          
      if root.left:
        dfs(root.left, [str(root.val) + "->"])
      if root.right:
        dfs(root.right, [str(root.val) + "->"])
      
      if not root.left and not root.right:
        ans.append(str(root.val))
      return ans