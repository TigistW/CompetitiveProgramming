class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for i in range(n)] for j in range(m)]

        for i in range(m):
          for j in range(n):
            # print(i,j)
            if i == 0 and j == 0:
              dp[0][0] = 1
            elif i == 0:
              dp[i][j] += dp[i][j - 1]
            elif j == 0:
              dp[i][j] += dp[i - 1][j]
            else:
              dp[i][j] += dp[i - 1][j] + dp[i][j - 1]
        return dp[m - 1][n - 1]