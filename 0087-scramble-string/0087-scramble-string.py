class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        @lru_cache(None)
        def f(a:int, b:int, x:int, y:int) -> bool:
            if a == b:
                return s1[a] == s2[x]

            res = False
            k = b-a+1 
            for m in range(k-1):
                res = res or (f(a, a+m, x, x+m) and f(a+m+1, b, x+m+1, y))
                res = res or (f(a, a+m, y-m, y) and f(a+m+1, b, x, x+k-m-2))
            
            return res

        return f(0, len(s1)-1, 0, len(s2)-1)