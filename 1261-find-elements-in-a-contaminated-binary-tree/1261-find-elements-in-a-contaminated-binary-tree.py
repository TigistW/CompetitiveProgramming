# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
      self.set_nodes = set()
      self.set_nodes.add(0)
      
      self.root = root
      queue = deque()
      self.root.val = 0
      queue.append(self.root)
      
      while queue:
        for i in range(len(queue)):
          cur = queue.popleft()
          if cur.left:
            cur.left.val = (cur.val * 2) + 1
            queue.append(cur.left)
            self.set_nodes.add(cur.left.val)
          if cur.right:
            cur.right.val = (cur.val * 2) + 2
            queue.append(cur.right)
            self.set_nodes.add(cur.right.val)
            
    def find(self, target: int) -> bool:
      if target in self.set_nodes:
        return True
      return False

# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)