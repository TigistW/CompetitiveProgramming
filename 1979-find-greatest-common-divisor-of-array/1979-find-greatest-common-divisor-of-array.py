class Solution:
    def findGCD(self, nums: List[int]) -> int:
        def gcd(one, two):
            maxx = -math.inf
            for i in range(1, one + 1):
                if int(two / i) == (two / i) and int(one / i) == (one / i):
                    maxx = max(maxx, i)
            return maxx 
        return gcd(min(nums), max(nums))