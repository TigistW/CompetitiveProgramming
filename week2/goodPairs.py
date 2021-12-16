#https://leetcode.com/problems/number-of-good-pairs/

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        n=len(nums)
        counter=0
        for i in range(n):
            for j in range(n):
                if i<j:
                    if(nums[i]==nums[j]):
                        counter+=1
        return counter
                    