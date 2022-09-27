class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
      
        total = sum(stones)
        dp = [False for i in range((total // 2) + 1)]
        dp[0] = True
        maxx = 0
        for i in stones:
          cur = dp.copy()
          for j in range(i, (total // 2) + 1):
            if dp[j - i]:
              cur[j] = True
              maxx = max(j, maxx)
              if j == total // 2:
                return total  - (2 * j)
          dp = cur
        # print(dp)
        return total - (maxx * 2)
            
        