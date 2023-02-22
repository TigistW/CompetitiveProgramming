class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        hash = [0 for i in range(60)]
        for i in range(len(time)):
            hash[time[i] % 60] += 1
        ans = 0
        for i in range(1, 30):
            ans += (hash[i] * hash[60 - i])
        ans += ((hash[0] * (hash[0]  - 1))  // 2 )
        ans += ((hash[30] * (hash[30]  - 1))  // 2 )
        return ans
        