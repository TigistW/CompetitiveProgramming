class Solution:
    @lru_cache(maxsize=None)
    def numTrees(self, n: int) -> int:
        if n <= 1:
            return 1
        
        return sum(self.numTrees(rootNum-1) * self.numTrees(n-rootNum) for rootNum in range(1, n+1))