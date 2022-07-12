class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []
        for i in logs:
          if i == "../":
            if len(stack) > 0:
              stack.pop()
          elif i != "./":
            stack.append(i)
        return len(stack)