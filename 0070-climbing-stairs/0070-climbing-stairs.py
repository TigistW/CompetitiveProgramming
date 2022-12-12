class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0 for i in range(n + 1)]
        dp[0] = 1
        dp[1] = 1
        for i in range(2, n + 1):
          for j in range(1,3):
            dp[i] += dp[i - j]
        return dp[n]