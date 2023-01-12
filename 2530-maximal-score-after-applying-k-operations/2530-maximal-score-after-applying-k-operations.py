class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        nums = [-n for n in nums]
        heapify(nums)
        score = 0
        for _ in range(k):
            val = -heappop(nums)
            score += val
            heappush(nums, -ceil(val / 3))
        return score