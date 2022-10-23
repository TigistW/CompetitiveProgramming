class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        ans = [0,0]
        for i in range(1, len(nums) + 1):
          if i not in count:
            ans[1] = i
          if count[i] == 2:
            ans[0] = i
        # print(ans)
        return ans
            
          