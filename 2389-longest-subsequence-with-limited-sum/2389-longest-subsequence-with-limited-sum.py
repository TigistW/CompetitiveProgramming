class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        ans = []
        nums.sort()
        for i in queries:
          summ = 0
          count = 0
          for j in range(len(nums)):
            if summ + nums[j] <= i:
              summ += nums[j]
              count += 1
            else:
              ans.append(count)
              break
            if j == len(nums) - 1:
              ans.append(count)
        return ans
              
            
          
          