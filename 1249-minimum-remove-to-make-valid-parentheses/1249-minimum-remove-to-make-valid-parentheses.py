class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        ans = []
        
        for i in range(len(s)):
          if s[i].isalpha():
            ans.append(i)
          elif s[i] == "(":
            stack.append((s[i],i))
          else:
            if stack and stack[-1][0] == "(":
              stack.pop()
            else:
              stack.append((s[i],i))
              
        listed = list(s)
        # print(stack,listed)
        while stack:
          val = stack.pop()[1]
          listed.pop(val)
        return "".join(listed)
        
              
            