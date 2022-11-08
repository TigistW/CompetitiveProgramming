class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        
        for i in s:
          if not stack:
            stack.append(i)
          else:
            if not i == stack[-1] and (i.lower() == stack[-1] or stack[-1].lower() == i):
              stack.pop()
            else:
              stack.append(i)
        return "".join(stack)
          
              
              
            