# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        result = []
        queue = deque([root])
        
        while queue:
            level_size = len(queue)
            current_sum = 0
            
            for i in range(level_size):
                current_node = queue.popleft()
                current_sum += current_node.val 
                
                if current_node.left:
                    queue.append(current_node.left)
                if current_node.right:
                    queue.append(current_node.right)
                    
            result.append(current_sum / level_size)
            
        return result
                
                
                