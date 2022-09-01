class Solution(object):
    def searchInsert(self, nums, target):
      left = 0
      right = len(nums) - 1
      best = -1
      while left <= right:
        mid = left + (right - left) // 2
        best = mid
        # print(left,mid, right, nums[mid])
        if nums[mid] < target:
          # print("here")
          left = mid + 1
          # print(left)

        elif nums[mid] > target:
          right = mid - 1

        else:
          return best
        
      if nums[best] < target:
        return best + 1
      return best





        
        