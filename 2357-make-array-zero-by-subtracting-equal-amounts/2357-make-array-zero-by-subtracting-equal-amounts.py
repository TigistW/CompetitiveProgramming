class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        count = 0
        nums.sort()
        ptr = len(nums) + 1
        for i in range(len(nums)):
          if nums[i] != 0:
            ptr = i
            break
        
        while ptr < len(nums):
          val = nums[ptr]
          for i in range(ptr, len(nums)):
            nums[i] -= val
          while ptr < len(nums) and nums[ptr] == 0 :
            ptr += 1
          count += 1
        return count
            
            
          