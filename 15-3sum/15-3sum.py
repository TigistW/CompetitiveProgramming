class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums) -1 ):
          left = i + 1
          right = len(nums) - 1
          
          while left < right:
            if nums[left] + nums[right] + nums[i] == 0:
                res.append((nums[left],nums[right],nums[i]))
                left += 1
                right -= 1
            elif nums[left] + nums[right] + nums[i] < 0:
              left += 1
            else:
              right -= 1   
        return set(res)