class Solution:
    def countEven(self, num: int) -> int:
        count = 0
        for i in range(1,num + 1):
          string = str(i)
          summ = 0
          for j in string:
            summ += int(j)
            
          if summ % 2 == 0:
            count += 1
        return count
            
    