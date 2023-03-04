class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        answer = 0
        min_position = max_position = left_bound = -1
        for i, number in enumerate(nums):
            if number < minK or number > maxK:
                left_bound = i
            if number == minK:
                min_position = i
            if number == maxK:
                max_position = i
            answer += max(0, min(min_position, max_position) - left_bound)
            
        return answer