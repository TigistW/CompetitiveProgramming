class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        preSum = []
        preSum.append(0)
        for i in range(len(nums)):
          preSum.append(preSum[-1] + nums[i])
        preSum.append(0)
        # print(preSum)
        for i in range(1,len(preSum) - 1):
          if preSum[i - 1] == preSum[-2] - preSum[i]:
            return i - 1
        return -1
            
          
          