class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curMin, curMax = 1,1
        ans = max(nums)
        
        for i in nums:
          if i == 0:
            curMin, curMax = 1,1
            
          var = curMax * i
          curMax = max(i, curMin * i, curMax * i)
          curMin = min(i, curMin * i, var)
          
          
          ans = max(ans, curMax)
          # print(curMax,curMin,i)
        return ans
          
          
            