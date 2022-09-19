class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        preSum = []
        sufSum = []
        outSum = []
        preSum.append(1)
        for i in range(len(nums)):
          preSum.append(preSum[i] * nums[i])
        
        sufSum.append(1)
        for i in range(len(nums) - 1,-1,-1):
          sufSum.append(sufSum[len(nums) - 1 - i] * nums[i])
        
        sufSum = sufSum[::-1]
        
        for i in range(len(nums)):
          outSum.append(preSum[i] * sufSum[i + 1])
        return outSum
          
          
          
        