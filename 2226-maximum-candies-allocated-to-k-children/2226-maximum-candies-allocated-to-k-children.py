class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
      def helper(mid):
        count = 0
        if mid == 0:
          return k
        else:
          for i in range(len(candies)):
            count += candies[i] // mid
        return count
      
      left , best = 0 , 0
      right = max(candies)
      
      while left <= right:
        
        mid = left + (right - left) // 2
        cnt= helper(mid)
        # print(left,mid,right,cnt)
        
        if cnt >= k:
          best = mid
          left = mid + 1
        else:
          right = mid - 1
        # print(left,mid,right,cnt)
      return best
      
            