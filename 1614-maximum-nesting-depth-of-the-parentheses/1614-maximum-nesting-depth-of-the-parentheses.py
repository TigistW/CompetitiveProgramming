class Solution:
    def maxDepth(self, s: str) -> int:
        stack = []
        count = 0
        for i in s:
          if i == "(":
            stack.append("(")
            
          elif i == ")":
            count = max(count, len(stack))
            stack.pop()
            
          else:
            continue
            
        return count
          