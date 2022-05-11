class Solution:
    def numberOfSteps(self, num: int) -> int:
      counter = 0
      if num == 0:
        return 0
      while num:
        if num % 2 == 0:
          num = num / 2
          counter += 1
        if num % 2 != 0: 
          num -= 1
          num = num / 2
          counter += 2
      return counter -1 
            
            
            