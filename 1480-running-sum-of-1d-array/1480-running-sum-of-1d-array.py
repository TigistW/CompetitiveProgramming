class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
      running_sum = []
      summ = 0
      for i in nums:
          summ += i
          running_sum.append(summ)
          
      return running_sum
          
          