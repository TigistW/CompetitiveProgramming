class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        dp = [math.inf for i in range(n + 1)]
        dp[0] = 0
        
        for val in range(len(ranges)):
            left = max(0, val - ranges[val])
            right = min(n, val + ranges[val])
            for interval in range(left, right + 1):
                dp[interval] = min(dp[interval], dp[left] + 1)

        if dp[-1] == math.inf:
            return -1
        return dp[-1]