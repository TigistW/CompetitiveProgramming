# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, node: Optional[TreeNode]) -> bool: 
        if not node:
            return False
        
        queue = deque([node])
        
        while queue:
            level_size = len(queue)
            level_list = []
            
            for i in range(level_size):
                current_node = queue.popleft()
                
                if current_node:
                    queue.append(current_node.left)
                    queue.append(current_node.right)
                    level_list.append(current_node.val)
                else:
                    level_list.append(current_node)
                    
            if not self.isValid(level_list):
                return False
            
        return True
    
    def isValid(self, lis):
        for i in range(len(lis) // 2):
            if lis[i] != lis[len(lis) - i - 1]:
                return False

        return True 
                    
        
        
#         def bfs(node):
#             # if not node.left and not node.right:
#                 # return True
#             left = node.left
#             right = node.right   
#             l = lis.append(left.val)  
#             r = lis.append(right.val)
#             for i in range(len(lis)//2):
#                 if lis[0] != lis[-1]: 
#                     return False
#                 lis = lis[1:-1]
#             for i in range(len(lis)):
#                 lis.pop()
#             bfs(left)
#             bfs(right)  
#         lis = [] 
#         return bfs(node)
#         return True 
        
                
            
                
            
            