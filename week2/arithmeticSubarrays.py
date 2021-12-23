#https://leetcode.com/problems/arithmetic-subarrays/submissions/
class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        result=[]
        for i in range(len(l)):
            
            left = l[i]
            right = r[i]
            
            ans=self.check(nums[left:right+1])
            
            result.append(ans)
            
        return result
    
    def check(self,nums):
        if len(nums)==1:
            return True
        nums.sort()
        
        diff=nums[1]-nums[0]
        
        for i in range(len(nums)-1):
            if nums[i+1]-nums[i]!=diff:
                return  False
        return True
    