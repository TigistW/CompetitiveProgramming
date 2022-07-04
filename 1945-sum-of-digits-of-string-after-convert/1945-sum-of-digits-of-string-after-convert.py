class Solution:
    def getLucky(self, s: str, k: int) -> int:
        integer = ""
        for i in s:
          conv = str(ord(i) - 96)
          integer += conv 
        
        for i in range(k):
          summ = 0
          for i in integer:
            summ += int(i)
          integer = str(summ)
          
        return summ
            
          
            
          
          