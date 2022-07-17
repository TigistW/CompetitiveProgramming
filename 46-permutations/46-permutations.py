class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        
        present = [False] * len(nums)

        def dfs(path):
          if len(path) == len(nums):
            ans.append(path.copy())
            return

          for i, num in enumerate(nums):
            if present[i]:
              continue
              
            present[i] = True
            path.append(num)
            dfs(path)
            path.pop()
            present[i] = False

        dfs([])
        return ans