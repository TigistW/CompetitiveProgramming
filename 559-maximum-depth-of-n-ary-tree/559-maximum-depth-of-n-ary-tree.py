"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        
        def dfs (root,maxLen):

            for child in root.children:
                listt.append([child , maxLen + 1])
                dfs(child,maxLen + 1)
            # return maxLen
        
        listt = [[root,1]]
        # maxLen = 1
        if root:
            dfs(root,1)
        else:
            return 0
        # print(listt)
        listt.sort(key = lambda x : x[1])
    
        return listt[-1][1]
        
                
                
        
        