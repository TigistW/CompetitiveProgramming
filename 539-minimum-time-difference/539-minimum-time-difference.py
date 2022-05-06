class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        res = 60 * 24
        nums = sorted([int(tp[:2]) * 60 + int(tp[3:]) for tp in timePoints])

        for i,j in zip(nums, nums[1:]):
            res = min(res, j - i)
        # return res
        return min(res, 24 * 60 - nums[-1] + nums[0])