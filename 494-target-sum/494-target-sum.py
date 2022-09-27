class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}
        
        def targetSum(index, summ):
          if index == len(nums):
            if summ == target:
              return 1
            return 0
          if (index, summ) in dp:
            return dp[(index, summ)]
        
          dp[(index, summ)] = (targetSum(index + 1, summ + nums[index]) +
                               targetSum(index + 1, summ - nums[index]))
          return dp[(index, summ)]
        
        return targetSum(0,0)
          
      