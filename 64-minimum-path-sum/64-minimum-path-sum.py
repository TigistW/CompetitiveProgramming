class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
      rows = len(grid)
      cols = len(grid[0])
      left,up = 0,0
      dp = [["inf" for _ in range(cols)] for _ in range(rows)]
      dp[0][0] = grid[0][0]
      
      for i in range(rows):
        for j in range(cols):
          if i == 0 and j == 0: continue
            
          if i - 1 >= 0 and  i < rows:
            up =  dp[i - 1][j]
          else:
            up = 999
            
          if j - 1 >= 0 and j < cols:
            left =  dp[i][j - 1]
          else:
            left = 999
            
          if dp[i][j] == "inf":
            dp[i][j] = (min(int(left) , int(up)) + int(grid[i][j]))
          else:
            dp[i][j] = min(dp[i][j], int(left) , int(up)) + int(grid[i][j])
            
            
      # print(dp)
      return dp[rows - 1][cols - 1] 
