class Solution:
    def removeDuplicates(self, nums):
        if len(nums)<2:
            return len(nums)
        prev = 0
        for curr in range(1,len(nums)):
            if nums[curr]!=nums[prev]:
                prev+=1
                nums[prev]=nums[curr]
        return prev+1