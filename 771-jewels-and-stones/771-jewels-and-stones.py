class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jew  = set(jewels)
        count = 0
        for i in stones:
          if i in jew:
            count += 1
        return count
            
          
          