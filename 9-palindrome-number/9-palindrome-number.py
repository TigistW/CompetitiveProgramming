class Solution:
    def isPalindrome(self, x: int) -> bool:
        values = []
        if x < 10 and x >= 0:
          return True
        while True:
          quo = x // 10
          rem = x % 10 
          if quo >= 10:
            values.append(rem)
          else:
            values.append(rem)
            values.append(quo)
            break
          x = quo
          
        # print(values)
          
        for i in range(len(values)//2):
            if values[i] != values[-(i + 1)]:
                return False
        return True
            
            
            
            
            