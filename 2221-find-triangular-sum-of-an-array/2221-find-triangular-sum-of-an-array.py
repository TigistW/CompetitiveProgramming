class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        if len(nums) == 1:
          return nums[0]
        length = len(nums)
        dp = [[0 for i in range(length - i)]  for i in range(length)]
        
        for i in range(length):
          for j in range(length - i):
            if i == 0:
              dp[i][j] = nums[j] % 10
              
            else:
              dp[i][j] = (dp[i - 1][j] + dp[i - 1][j + 1]) % 10
              
        # print(dp)
        return dp[-1][0]
              