class Solution:
    def breakPalindrome(self, palindrom: str) -> str:
      palindrom = list(palindrom)
      if len(palindrom) == 1:
        return ""
      if len(palindrom) % 2 != 0:
        if len(set(palindrom)) == 2:
          if palindrom[0] == 'z':
            palindrom[0] = "a"
            return "".join(palindrom)
          elif palindrom[0] == 'a':
            palindrom[-1] = chr(ord(palindrom[-1]) + 1)
            return "".join(palindrom)
          else:
            palindrom[0] = "a"
            return "".join(palindrom)
          
      if len(set(palindrom)) == 1:
        if palindrom[-1] == "z":
          palindrom[0] = "a"
          return "".join(palindrom)
        elif palindrom[-1] == "a":
          palindrom[-1] = chr(ord(palindrom[-1]) + 1)
          return "".join(palindrom)
        else:
          palindrom[0] = "a"
          return "".join(palindrom)
        
      i = 0
      while i < len(palindrom):
        if palindrom[i] == "a":
          # print(palindrom[i])
          i += 1
        else:
          break
      # print(i)
      if len(palindrom) % 2 != 0 and i == len(palindrom) // 2:
        palindrom[(len(palindrom) // 2) + 1] = "a"
        return "".join(palindrom)
      else:
        palindrom[i] = "a"
        return "".join(palindrom)
      
      
      
      
        
      
      