class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        ans = rem = prefixSum = 0
        mp = {0 : 1}

        for i in nums:
            prefixSum += i
            rem = prefixSum % k
            if(rem < 0):
                rem += k

            if rem in mp:
                ans += mp[rem]
                mp[rem] += 1
            else:
                mp[rem] = 1

        return ans