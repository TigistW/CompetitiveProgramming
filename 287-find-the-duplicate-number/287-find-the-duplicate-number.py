class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
      left = 0
      right = len(nums) - 1
      count , best= 0,0
      while left <= right:
        mid = left + (right - left )// 2
        for i in nums:
          if i <= mid:
            count += 1
        
        if count > mid:
          right = mid - 1
          best = mid
        else:
          left = mid + 1
        count = 0
      return best
          

            
    
            
            
            
            
            
                
            
                