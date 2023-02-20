class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        val = -math.inf
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[j] - nums[i] > val and i < j and nums[i] < nums[j]:
                    val = nums[j] - nums[i]
        if val == - math.inf:
            return -1
        return val