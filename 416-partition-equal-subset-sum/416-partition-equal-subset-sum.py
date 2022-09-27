class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        dp = [False for i in range((total //2) + 1)]
        dp[0] = True
        if total % 2 != 0:
          return False
        
        for num in nums:
          for i in range(total // 2 ,0 , -1):         
            if i >= num:
              dp[i] = dp[i] or dp[i - num]

        # print(dp)
        return dp[total // 2]
              
            