class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
      odd, even = 0, 0 
      
      for i in range(len(nums)- 1,-1,-1):
    
        curr_odd = max(even - nums[i], odd)
        curr_even = max(odd + nums[i], even)
        
        odd = curr_odd
        even = curr_even 
        
      return even
        