import math
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        min_vals = []
        ans = []
        for i in range(len(arr)):
          min_vals.append((i, math.fabs(x - arr[i])))
          
        min_vals.sort(key = lambda x:x[1])
        for i in range(k):
          ans.append(arr[min_vals[i][0]])
        ans.sort()
        
        return ans