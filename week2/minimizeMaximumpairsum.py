#https://leetcode.com/problems/minimize-maximum-pair-sum-in-array/
class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        li=[]
        n=len(nums)
        for i in range(n//2):
            li.append(nums[0]+nums[-1])
            nums.pop(0)
            nums.pop()
        return max(li)
     