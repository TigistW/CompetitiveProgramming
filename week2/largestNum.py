#https://leetcode.com/problems/largest-number/ 
class Solution:
    def largestNumber(self, nums):
        res=''
        nums = sorted([str(n) for n in nums], reverse=True)
        for i in range(len(nums)-1):
            j=i
            while int(res+str(nums[j])+str(nums[j+1])) < int(res+str(nums[j+1])+str(nums[j])) and j>-1:
                nums[j],nums[j+1] = nums[j+1],nums[j]
                j-=1
        if int(''.join(nums)) == 0:
            return str(0)
        return ''.join(nums)