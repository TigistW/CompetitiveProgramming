class Solution:
    def numDecodings(self, s: str) -> int:
        dp = { len(s) : 1}
        for i in range(len(s) - 1, -1, -1):
          if s[i] == "0":
            dp[i] = 0
          else:
            dp[i] = dp[i + 1]
            
            if (i + 1 < len(s) and int(s[i:i + 2]) <= 26):
                dp[i] += dp[i + 2]
        # print(dp)
        return dp[0]