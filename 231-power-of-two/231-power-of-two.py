import math
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
          return False
        num = math.log2(n)
        if num.is_integer():
          return True
        return False
      

  