class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        
        if int(math.sqrt(num) + 0.5) ** 2 == num:
          return True
        return False