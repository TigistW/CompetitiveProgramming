class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        dp = [[0 for i in range(i)] for i in range(1,numRows + 1)]
        
        for i in range(numRows):
          for j in range(i + 1):
            if i == 0 and j == 0:
              dp[i][j] = 1
            elif j == 0:
              dp[i][j] = dp[i - 1][j]
            elif j == i:
              dp[i][j] = dp[i - 1][j - 1]
            else:
              dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
        return dp
            
              
              