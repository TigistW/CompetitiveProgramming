class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        maxi = 0
        for i in range(n//2):
            maxi = max(maxi,nums[i] + nums[n - i - 1])
        return maxi