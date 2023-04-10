class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        braces = {"(":")","[":"]","{":"}"}
        
        rev = {")":"(", "]":"[", "}":"{"}
        
        for i in s:
          if i in braces:
            stack.append(i)
          else:
            val = rev[i]
            if stack:
              if stack[-1] != val:
                return False
              else:
                stack.pop()
            else:
              return False
        if stack:
          return False
        return True