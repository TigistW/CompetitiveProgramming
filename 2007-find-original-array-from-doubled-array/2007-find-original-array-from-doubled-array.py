from collections import Counter
class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        ans = []
        count = Counter(changed)
        if count[0] % 2 != 0 or len(changed) % 2 != 0:
          return []
        
        for i in sorted(changed):
          if i in count:
            if count[i] > 0:
              count[i] -= 1
              if i * 2 in count:
                if count[i * 2] > 0:
                  count[i * 2] -= 1
                  ans.append(i)
        if len(ans) == len(changed) // 2:
          return ans
        return []
