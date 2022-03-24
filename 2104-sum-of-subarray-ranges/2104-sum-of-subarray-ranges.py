class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        res , largest , smallest = 0 , 0 , nums[0];
        current_size = len(nums)
        start_pos = 0
        for i in range(current_size):
            largest = nums[i]
            smallest = nums[i]
            for j in range(start_pos,current_size):
                largest = max(largest,nums[j])
                smallest = min(smallest,nums[j])
                res += (largest - smallest)
            start_pos += 1
        return res
            
        
        