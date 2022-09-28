class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
     # memo = {}
        @lru_cache(None)
        def dp(d, target):
            if d == 0:
                return 0 if target > 0 else 1
            # if (d, target) in memo:
            #     return memo[(d, target)]
            to_return = 0
            for m in range(max(0, target-k), target):
                to_return += dp(d-1, m)
            # memo[(d, target)] = to_return
            return to_return
        return dp(n, target) % (10**9 + 7)