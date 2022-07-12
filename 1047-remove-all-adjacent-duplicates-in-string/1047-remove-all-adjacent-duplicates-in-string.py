class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        
        for i in s:
          if len(stack) == 0:
            stack.append(i)
          else:
            if i == stack[-1]:
              stack.pop()
            else:
              stack.append(i)
        return "".join(stack)
          
        