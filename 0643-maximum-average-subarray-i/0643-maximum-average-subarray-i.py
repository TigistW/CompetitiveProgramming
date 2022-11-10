class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        left = 0
        right = k - 1
        avg = - math.inf
        summ = sum(nums[left:right + 1])
        while right <= len(nums) - 1:
            avg = max(avg, summ / k)
            if right == len(nums) - 1:
              break
            right += 1
            summ += nums[right]  
            summ -= nums[left]
            left += 1
        return avg