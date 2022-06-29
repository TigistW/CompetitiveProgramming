class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
      
      hashset = set()
      
      hashsettwo = set()
      hashtable = dict()
      if len(s) != len(t):
        return False
      
      for i in range(len(s)):
        if s[i] not in hashset:
          if t[i] not in hashsettwo:
            hashtable[s[i]] = t[i]
            hashset.add(s[i])
            hashsettwo.add(t[i])
          else:
            return False
        else:
          if hashtable[s[i]] == t[i]:
            continue
          else:
            return False
      return True
            
      
      
        