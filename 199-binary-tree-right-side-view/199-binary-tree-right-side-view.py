# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue = deque()
        queue.append(root)
        ans = []
        if not root:
          return []
        while queue:
          level_size = len(queue)
          level_list = 0
          for i in range(level_size):
            num = queue.popleft()
            if i == level_size - 1:
              level_list = num.val
            if num.left:
              queue.append(num.left)
            if num.right:
              queue.append(num.right)         
          ans.append(level_list)
        return ans
            