class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
      rows = len(dungeon)
      cols = len(dungeon[0])
      dp = [[0 for _ in range(cols)] for _ in range(rows)]
      
      for i in range(rows - 1,-1,-1):
        for j in range(cols - 1,-1,-1):
          # print(i,j)
          if i == rows - 1 and j == cols - 1:
            dp[i][j] = min(0, dungeon[i][j])  
          elif i == rows - 1:
            dp[i][j] = min(0, dungeon[i][j] + dp[i][j + 1])
          elif j == cols - 1:
            dp[i][j] = min(0, dungeon[i][j] + dp[i + 1][j])
          else:
            dp[i][j] = min(0, dungeon[i][j] + max(dp[i][j + 1],dp[i + 1][j]))
            
      print(dp)        
      return abs(dp[0][0]) + 1
          
          

                
              
