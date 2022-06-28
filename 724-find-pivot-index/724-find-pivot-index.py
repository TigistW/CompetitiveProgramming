class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
      summation = []
      summ = 0
      for i in range(len(nums) - 1,-1,-1):
        summ += nums[i]
        summation.append(summ)
        
      summation.reverse()
      
      summ2 = 0
      summation2 = []
      for i in range(len(nums)):
        summ2 += nums[i]
        summation2.append(summ2)

      
      for i in range(len(summation)):
        if summation[i] == summation2[i]:
          return i
      return -1
        