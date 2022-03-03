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
            cur_sum = 0
            
            for i in range(level_size):
                cur_num = queue.popleft()
                if cur_num:
                    cur_sum += cur_num.val
                    if cur_num.left:
                        queue.append(cur_num.left)
                    if cur_num.right:
                        queue.append(cur_num.right)
                        
            result.append(cur_sum/level_size)
        return result  
                
                
                