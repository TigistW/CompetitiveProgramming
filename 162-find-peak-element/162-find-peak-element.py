class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        if len(nums) == 1:
          return 0
        while left <= right:
          mid = (left + right) // 2
          if mid == 0:
            if nums[mid] > nums[mid + 1]:
              return mid
            elif nums[mid] < nums[mid + 1]:
              left = mid + 1
              
          if mid == len(nums) - 1:
            if nums[mid] > nums[mid - 1]:
              return mid
            elif nums[mid] < nums[mid - 1]:
              right = mid - 1
          
          elif mid != 0 and mid != len(nums) - 1:
            if nums[mid - 1] <  nums[mid] and nums[mid] < nums[mid + 1]:
              left = mid + 1

            elif nums[mid - 1] >  nums[mid] and nums[mid] < nums[mid + 1]:
              right = mid - 1

            elif nums[mid - 1] >  nums[mid] and nums[mid] > nums[mid + 1]:
              right = mid - 1

            elif nums[mid - 1] <  nums[mid] and nums[mid] > nums[mid + 1]:
              return mid




            