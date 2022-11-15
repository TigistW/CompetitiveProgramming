# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        queue = deque()
        queue.append(root)
        count = 0
        if not root:
          return 0
        while queue:
          for i in range(len(queue)):
            cur = queue.popleft()
            if cur.left:
              queue.append(cur.left)
            if cur.right:
              queue.append(cur.right)
              
            count += 1
            
        return count
              