class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        largest = 0
        dp = [[0 for _ in range(cols + 1)] for _ in range(rows + 1)]
        
        for i in range(len(dp)):
          for j in range(len(dp[0])):
            if i == 0 or j == 0:
              dp[i][j] = 0
            else:
              if int(matrix[i - 1][j - 1]) == 0:
                dp[i][j] = 0
              else:
                dp[i][j] = min(dp[i - 1][j],dp[i][j - 1],dp[i - 1][j - 1]) + int(matrix[i - 1][j - 1])
            largest  =max(largest, dp[i][j])
        print(dp)
        return largest * largest
              
          
        
        