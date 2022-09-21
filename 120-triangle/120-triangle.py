class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        val = len(triangle)
        upleft, upparallel = 0,0
        dp = [["inf" for j in range(len(triangle[i]))] for i in range(val)]
        
        
        dp[0][0] = triangle[0][0]
        
        for i in range(len(triangle)):
          for j in range(len(triangle[i])):
            
            if i == j:
              upparallel = 10001
            else:
              upparallel = dp[i - 1][j]
              
            if j == 0:
              upleft = 10001
            else:
              upleft = dp[i - 1][j - 1]
              
              
            if i == 0 and j == 0: continue
            else:
              if dp[i][j] == "inf":
                dp[i][j] = min(upparallel,upleft) + triangle[i][j]
              else:
                dp[i][j] = min(dp[i][j],upparallel,upleft) + triangle[i][j]
        return min(dp[-1])
              
            
        