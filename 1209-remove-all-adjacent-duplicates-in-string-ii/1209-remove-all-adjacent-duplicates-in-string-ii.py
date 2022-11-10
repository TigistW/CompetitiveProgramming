class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        
        for i in s:
          count = k
          if not stack:
            stack.append((i, 1))
          else:
            if i == stack[-1][0]:
              if (stack[-1][1] + 1) == count:
                while count - 1:
                  stack.pop()
                  count -= 1
              else:
                stack.append((i, stack[-1][1] + 1))
            else:
              stack.append((i, 1))
        
        res = ""
        for i in stack:
          res += i[0]
        return res