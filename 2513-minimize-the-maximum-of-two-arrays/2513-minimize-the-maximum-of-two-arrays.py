class Solution:
    def bs(self, num,  d1, d2, cnt1, cnt2):
        both = num // lcm(d1, d2)
        first = num // d1
        second = num // d2

        both_add = num - (first + second - both)

        cnt1 = max(0, cnt1 - (second - both))
        cnt2 = max(0, cnt2 - (first - both))

        return both_add >= cnt1 + cnt2

    def minimizeSet(self, divisor1: int, divisor2: int, uniqueCnt1: int, uniqueCnt2: int) -> int:
        low, high = 0, 10**11
        while low + 1 < high:
            mid = (low + high) // 2
            if self.bs(mid,  divisor1, divisor2, uniqueCnt1, uniqueCnt2):
              high = mid                       
            else:
              low = mid                
        return high