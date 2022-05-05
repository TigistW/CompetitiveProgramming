class Solution:
    def minNonZeroProduct(self, p: int) -> int:
        end = 2**p -1
        m = 10**9 + 7
        return (pow(end-1, end//2, m) * end)%m
        