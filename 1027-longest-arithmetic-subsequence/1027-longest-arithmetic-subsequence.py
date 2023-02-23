class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        dp = [dict() for _ in range(len(nums))]
        ans = 2
        for j in range(len(nums)):
            for i in range(j):
                if nums[j] - nums[i] in dp[i]:
                    dp[j][nums[j] - nums[i]] = dp[i][nums[j] - nums[i]] + 1
                else:
                    dp[j][nums[j] - nums[i]] = 2
                ans = max(ans, dp[j][nums[j] - nums[i]])
        return ans