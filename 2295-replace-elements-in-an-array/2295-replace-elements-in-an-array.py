class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        dic = defaultdict()
        for idx, i in enumerate(nums):
          dic[i] = idx
        
        for num, sub in operations:
          if num in dic:
            nums[dic[num]] = sub
            dic[sub] = dic[num]
        return nums