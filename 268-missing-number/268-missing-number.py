class Solution:
    def missingNumber(self, nums: List[int]) -> int:
      ans = len(nums)
      for i, num in enumerate(nums):
        # print(i,num)
        # print((i ^ num)^3)
        # ans ^= i ^ num
        ans = ans ^ (i^num)
      return ans
       