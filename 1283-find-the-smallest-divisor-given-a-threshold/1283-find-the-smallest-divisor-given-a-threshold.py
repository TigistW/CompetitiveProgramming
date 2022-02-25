class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        left = 1
        right = max(nums)
        summ=0
        
        while(left <= right):
            mid = left + (right - left)//2
            for num in nums:
                summ += math.ceil(num/mid)
            
            if summ > threshold:
                left = mid + 1
            else:
                right = mid - 1
            summ=0
        return left

            