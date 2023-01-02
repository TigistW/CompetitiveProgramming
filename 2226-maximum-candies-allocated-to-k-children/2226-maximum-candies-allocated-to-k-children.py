class Solution:
    def assist(self, candies, n):
      count = 0
      for i in candies:
        count += (i// n)
      return count
        
    def maximumCandies(self, candies: List[int], k: int) -> int:
        left = 1
        right = max(candies)
        ans = 0

        while left <= right:
          mid = (left + right) // 2
          val = self.assist(candies, mid)
          # print(left, mid, right, val)
          if val >= k:
            ans = max(ans, mid)
            left = mid + 1
            # print("go right")
          else:
            right = mid - 1
            # print("go left")
          # print(left, mid, right, val)
        return ans
            
            