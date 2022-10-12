class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        
        for i in range(len(nums) - 1, -1, -1):
          # print(nums[i],nums[i - 1],nums[i - 2])
          if nums[i] + nums[i - 1] > nums[i - 2] and nums[i - 1] + nums[i - 2] > nums[i] and nums[i] + nums[i - 2] > nums[i - 1]:
            return nums[i] + nums[i - 1] + nums[i - 2]
          
        return 0
          