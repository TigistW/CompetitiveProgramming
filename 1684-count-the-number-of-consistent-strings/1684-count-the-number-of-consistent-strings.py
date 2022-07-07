class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        sets = set(list(allowed))
        count = len(words)
        for i in words:
          for j in i:
            if j not in sets:
              count -= 1
              break 
        return count
            
              
              
          
              
              
              
            
          
            
            