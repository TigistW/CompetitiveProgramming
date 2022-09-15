class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = left + 1
        
        maxProfit = float('-inf')
        for i in range(len(prices) - 1):
          runningProfit = prices[right] - prices[left]
          maxProfit = max(maxProfit, runningProfit) 
          
          while right - left >= 1:
            if prices[right] - prices[left] < 0:
              left += 1
              maxProfit = max(maxProfit,prices[right] - prices[left])
            else:
              break   
          right += 1
        if maxProfit < 0: 
          return 0
        return maxProfit
          
          
            
            
            
          
          
          
          
          
          
          
          
          
          
          