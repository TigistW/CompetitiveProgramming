class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for i in s:
          if not stack:
            stack.append(i)
          else:
            if i == stack[-1]:
              stack.pop()
            else:
              stack.append(i)
        return "".join(stack)
        