class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        
        for i in s:
          if len(stack) == 0: 
            stack.append(i)
          else:
            if i.islower():
              if stack[-1].isupper():
                if stack[-1].lower() == i:
                  stack.pop()
                else:
                  stack.append(i)
              else:
                stack.append(i)
                
            else:
              if stack[-1].islower():
                if stack[-1].upper() == i:
                  stack.pop()
                else:
                  stack.append(i)
              else:
                stack.append(i)
    
        return "".join(stack) 
              
              
            