class Solution:
    def minimumSum(self, num: int) -> int:
        vals = []
        summ = 0
        while num:
          quo = num // 10
          rem = num % 10
          
          vals.append(rem)
          num = quo
          
        vals.sort()
        
        for i in range(2):
          val = vals.pop(-1) 
          summ += val
          
        for i in vals:
          summ += (i * 10)
          
        return summ
             
        
        
          
          
          
        
        
        
          
        
        
        