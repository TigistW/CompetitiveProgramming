class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        jumped = 0
        
        for i in range(n - 1):
            
            jumped = max(jumped, i + nums[i])
            if jumped == i: 
                return False
            if jumped >= n - 1: 
                return True
            
        return True
            
    
    
    
    