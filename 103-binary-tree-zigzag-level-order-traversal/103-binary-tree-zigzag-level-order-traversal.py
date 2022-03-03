# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        result = []
        queue = deque([root])
        left_to_right = True
        
        while queue:
            level_size = len(queue)
            current_list = deque()
            
            for i in range(level_size):
                current_node = queue.popleft()
                
                if left_to_right:
                    current_list.append(current_node.val)
                else:
                    current_list.appendleft(current_node.val)
                
                if current_node.left:
                    queue.append(current_node.left)
                if current_node.right:
                    queue.append(current_node.right)
                    
            left_to_right = not left_to_right
            result.append(current_list)
            
        return result
                
                
                    
                    
            
            