class Solution:
    def days(self, weights, k):
      ans = 0
      ship = 0
      
      for w in weights:
        if ship + w <= k:
          ship += w
        else:
          ship = w
          ans += 1
      
      return ans + 1
        
    def shipWithinDays(self, weights: List[int], days: int) -> int:
      l = max(weights)
      r = sum(weights)
      best = None
      
      while l <= r:
        mid = l + (r - l) // 2
        days_mid = self.days(weights, mid)
        
        if days_mid <= days:
          r = mid - 1
          best = mid
        else:
          l = mid + 1
      
      return best