class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        ans = 0
        minAvailable = 0
        nums.sort()
        for i in nums:
            ans += max(minAvailable - i, 0)
            minAvailable = max(minAvailable, i) + 1
        return ans
