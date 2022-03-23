# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        result = []
        biggest = float('-inf')
        queue = deque([root])
        while queue:
            level_size = len(queue)
            for i in range(level_size):
                current_node = queue.popleft()
                if current_node.val > biggest:
                    biggest = current_node.val
                if current_node.left:
                    queue.append(current_node.left)
                if current_node.right:
                    queue.append(current_node.right)
            result.append(biggest)  
            biggest = float('-inf')   
        return result