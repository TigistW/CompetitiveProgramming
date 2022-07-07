import math
class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        count = 0
        size = len(nums)
        for i in range(size):
          for j in range(size):
            if i < j:
              if math.fabs(nums[i] - nums[j]) == k:
                count += 1
        return count
                