class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        size = len(nums)
        return nums[size // 2]