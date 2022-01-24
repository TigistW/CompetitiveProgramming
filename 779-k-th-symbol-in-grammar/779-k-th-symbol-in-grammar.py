class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        def bitts(n):
            res = 0
            while n:
                n &= n - 1
                res += 1
            return res
        return bitts(k-1) % 2