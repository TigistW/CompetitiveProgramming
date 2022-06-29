class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1 
        index = 0
        
        while start <= end:
          mid = start + (end - start) // 2
          
#           print("start", start,"middle",mid,"end",end)
          
          if nums[mid] == target:
            index = mid
            return index
            
          if nums[mid] < target:
            index = mid + 1
            start = mid + 1
          
          if nums[mid] > target:
            index = mid
            end = mid - 1
        return index
            
          
            
        
            
          
        