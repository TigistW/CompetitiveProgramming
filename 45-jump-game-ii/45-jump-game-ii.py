class Solution:
  def jump(self, nums: List[int]) -> int:
    res = 0
    end = 0
    longest = 0
    for i in range(len(nums) - 1):
      longest = max(longest, i + nums[i])
      if longest >= len(nums) - 1:
        res += 1
        break
      if i == end:
        res += 1 
        end = longest
    return res
