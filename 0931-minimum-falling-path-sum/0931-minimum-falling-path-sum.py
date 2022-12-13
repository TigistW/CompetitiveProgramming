class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        rows = len(matrix)
        cols = rows
        dp = [[float(inf) for i in range(cols)] for j in range(rows)]
        
        for i in range(rows):
          for j in range(cols):
            if i == 0:
              dp[i][j] = matrix[i][j]
              continue
            if j == 0:
              dp[i][j] = min(dp[i - 1][j],dp[i - 1][j + 1]) + matrix[i][j]
            elif j == cols - 1:
              dp[i][j] = min(dp[i - 1][j],dp[i - 1][j - 1]) + matrix[i][j]
            else:
              dp[i][j] = min(dp[i - 1][j],dp[i - 1][j - 1],dp[i - 1][j + 1]) + matrix[i][j]
        return min(dp[-1])
              
              
              