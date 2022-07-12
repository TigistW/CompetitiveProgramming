class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        res = []
        discount = 0
        for i in range(len(prices)):
          for j in range(i + 1, len(prices)):
            if prices[j] <= prices[i]:
              discount = prices[j]
              break
          res.append(prices[i] - discount)
          discount = 0
        return res
              
              
          
          