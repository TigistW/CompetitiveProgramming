class Solution:
    def maxArea(self, height: List[int]) -> int:
      left =  0
      right = len(height) - 1
      
      totalWater = 0
      while left < right:
        compWater = min(height[left], height[right]) * (right - left)
        totalWater = max(compWater,totalWater)
        
        if height[left] <= height[right]:
          left += 1
        else:
          right -= 1
          
      return totalWater
        
          
          
        
        
        
        