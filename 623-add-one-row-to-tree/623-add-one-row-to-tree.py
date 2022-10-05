# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
          newNode = TreeNode()
          newNode.val = val
          newNode.left = root
          
          return newNode
        
        queue = deque()
        queue.append(root)
        
        level_list = 1
        while queue and level_list != depth - 1:
          len_queue = len(queue)
          for i in range(len_queue):
            cur = queue.popleft()
            if cur.left:
              queue.append(cur.left)
            if cur.right:
              queue.append(cur.right)

          level_list += 1
        # print(queue)
        for i in range(len(queue)):
          
          cur = queue.popleft()
          
          cur_left = cur.left
          cur_right = cur.right
          
          new_cur_left = TreeNode()
          new_cur_left.val = val
          new_cur_left.left = cur_left
          
          
          new_cur_right = TreeNode()
          new_cur_right.val = val
          new_cur_right.right = cur_right
          
          cur.left = new_cur_left
          cur.right = new_cur_right
          
        return root
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
        
          
        