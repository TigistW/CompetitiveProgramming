class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        nums = []
        res = 0
        for i in range(n):
          num = start + 2 * i
          nums.append(num)
           
        for i in nums:
          res ^= i
        return res
          
        
        
        