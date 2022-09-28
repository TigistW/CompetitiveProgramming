class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        @lru_cache(None)
        def dp(n, target):
            if n == 0:
                return 0 if target > 0 else 1
            val = 0
            for m in range(max(0, target - k), target):
                val += dp(n-1, m)
            return val
        return dp(n, target) % (10**9 + 7)