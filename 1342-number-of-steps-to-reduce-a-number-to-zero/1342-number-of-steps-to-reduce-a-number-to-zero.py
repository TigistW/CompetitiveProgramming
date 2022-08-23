class Solution:
    def numberOfSteps(self, num: int) -> int:
      
      count = 0
      while num:
        if num % 2 != 0:
          count += 1
          num -= 1
          
        else:
          num /= 2
          count += 1
          
      return count
          
          
          
          
        
        
        
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
#         counter = 0
#         while num:
#           if (num and 1) == 0:
#             num = num >> 1
#           else:
#             num = num and ( ~(1)) 
#           counter += 1
#         return counter