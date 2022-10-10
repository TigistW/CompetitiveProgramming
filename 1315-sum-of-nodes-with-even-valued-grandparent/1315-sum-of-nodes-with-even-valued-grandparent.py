# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        queue = deque()
        queue.append(root)
        summ = 0
        while queue:
          for i in range(len(queue)):
            cur = queue.popleft()
            if cur.left:
              if cur.val % 2 == 0:
                if cur.left.left:
                  summ += cur.left.left.val
                if cur.left.right:
                  summ += cur.left.right.val
              queue.append(cur.left)


            if cur.right:
              if cur.val % 2 == 0:
                if cur.right.left:
                  summ += cur.right.left.val
                if cur.right.right:
                  summ += cur.right.right.val
              queue.append(cur.right)
              
        return summ

          