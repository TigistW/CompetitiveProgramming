# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        queue = deque()
        queue.append(root)
        count = 0
        
        while queue:
            count += 1
            size = len(queue)
            for i in range(size):  
                cur = queue.popleft()
                if cur == None:
                    return 0
                if cur.left:     
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
        return count
