class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr = 0
        maxx = nums[0]
        for i in range(0, len(nums)):
            if curr <0 :
                curr = 0
            curr += nums[i]
            maxx = max(maxx, curr)
        return maxx 