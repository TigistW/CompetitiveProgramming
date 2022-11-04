class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
      count = Counter(words)
      word = set(words)
      res = 0
      for i in words:
        if i == i[::-1]:
          if count[i] % 2 == 0:
            res += count[i]
            count[i] = 0
          else:
            res += count[i] - 1
            count[i] = 1
        else:
          if i[::-1] in word:
            res += 2 * (min(count[i], count[i[::-1]]))
            count[i] = 0
            count[i[::-1]] = 0
            
      for i in words:
        if i == i[::-1]:
          if count[i] == 1:
            res += 1
            break
      return res * 2
            
          
        
        
      
      
      
        

        
        
        
        
        
        
        
      
          
            
            
        