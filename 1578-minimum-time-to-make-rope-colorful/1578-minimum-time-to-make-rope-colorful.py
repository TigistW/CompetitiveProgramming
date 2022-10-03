class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        ans, left, right = 0, 0, 0
        
        while right < len(neededTime):
          cost = 0
          keep = 0
          
          while right < len(neededTime) and colors[left] == colors[right]:
            cost += neededTime[right]
            keep = max(keep, neededTime[right])
            right += 1
            
          left = right
          ans += cost - keep
          
        return ans
          