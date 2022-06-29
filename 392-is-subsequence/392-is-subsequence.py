class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        count = 0
        string = []
        
        if len(s) > len(t):
          return False
        for i in range(len(s)): 
          cur = s[i] 
          while count < len(t):
            letter = t[count]
            if cur == letter:
              string.append(cur)
              count += 1
              break
            else:
              count += 1
              
        subsequence = "".join(string)
        if subsequence == s:
          return True
        return False
      
              
              
              
          
          