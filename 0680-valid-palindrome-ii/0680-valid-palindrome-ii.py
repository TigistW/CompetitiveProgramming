class Solution:
    def validPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        count  = 0
        while left < right:
          if s[left] != s[right]:
              actual_value = s[left:right]
              left_deleted = s[left+1:right+1]
      
              if left_deleted == left_deleted[::-1] or actual_value == actual_value[::-1]:
                  return True
              return False
            
          else:
            left += 1
            right -= 1

        return True
          
            
            