class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
      @lru_cache(None)
      # dp = [[-1 for i in range(n)] for i in range(m)]
      def topDown(i,j,maxMove):
        if i >= m or j >= n or i < 0 or j < 0:
          return 1
        if maxMove == 0:
          return 0
        # if dp[i][j] in dp:
        #   return dp[i][j]
        dp = 0
        dp = (topDown(i + 1,j,maxMove - 1) + 
              topDown(i - 1,j,maxMove - 1)+
              topDown(i,j + 1,maxMove - 1)+
              topDown(i,j - 1,maxMove - 1))

        return dp
      return topDown(startRow,startColumn,maxMove) % ((10 ** 9) + 7)
      
      
        
        
        