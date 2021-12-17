
#https://leetcode.com/problems/array-with-elements-not-equal-to-average-of-neighbors/
class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        
        nums.sort()
        
        for val in range(len(nums)-1):
            if val%2==1:
                
                nums[val],nums[val+1]=nums[val+1],nums[val]
       
        return nums