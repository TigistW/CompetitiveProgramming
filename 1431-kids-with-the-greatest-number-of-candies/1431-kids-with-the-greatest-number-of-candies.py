class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        res = []
        
        for i in candies:
          if i + extraCandies >= max(candies):
            res.append(True)
          else:
            res.append(False)
        return res
            