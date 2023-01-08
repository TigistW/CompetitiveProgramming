class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos = []
        neg = []
        res = []
        for i in nums:
          if i < 0:
            neg.append(i)
          else:
            pos.append(i)
        i = 0
        for i in range(len(nums) // 2):
          res.append(pos[i])
          res.append(neg[i])
          i += 1
        return res
        