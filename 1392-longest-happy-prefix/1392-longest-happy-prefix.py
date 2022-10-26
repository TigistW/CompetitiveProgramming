class Solution:
    def longestPrefix(self, s: str) -> str:
        i = 0
        j = 1 
        li = [0] * len(s)
        while j < len(s):
          i = li[j - 1]
          while i > 0 and s[i] != s[j]:
            i = li[i - 1]
          if s[i] == s[j]:
            li[j] = i + 1
          j += 1
        # print(li)
        return s[:li[-1]]
            
        