class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        N=len(nums)
        for i in range(N):
             if nums[i]==nums[i+1]:
                    return nums[i]
                
            
                