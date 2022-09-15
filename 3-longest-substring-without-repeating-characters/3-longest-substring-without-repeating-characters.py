class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
      count = 0
      left = 0
      right = left + 1
      
      while right <= len(s):
        stri = s[left:right + 1]
        if len(stri) == len(set(stri)):
          count = max(count, len(stri))
          right += 1
        else:
          left += 1
      return count
        
        
        
      
      
      



          
          
          
          
          