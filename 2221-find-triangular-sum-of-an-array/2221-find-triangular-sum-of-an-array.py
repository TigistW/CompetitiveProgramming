class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        if len(nums) == 1:
          return nums[0]
        length = len(nums)
        dp = []
        for i in range(length):
          temp = [0 for i in range(length - i)]
          for j in range(length - i):
            if i == 0:
              temp[j] = nums[j] % 10 
            else:
              temp[j] = (dp[j] + dp[j + 1]) % 10
          dp = temp
        return dp[-1]
              