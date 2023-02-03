# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        li = []
        col, level = 0, 0
        queue = deque([[col,level,root]])
        while queue:
            for i in range(len(queue)):
                col,level,rt = queue.popleft()
                
                if rt.left:
                    queue.append([col - 1, level + 1,rt.left])
                if rt.right:
                    queue.append([col + 1,level + 1,rt.right])
                    
                li.append([col,level,rt.val])
        
        li.sort()
        res = [[li[0][2]]]
        for i in range(1,len(li)):
            if li[i][0] == li[i-1][0]:
                res[-1].append(li[i][2])
            else:
                res.append([li[i][2]])
        return res
