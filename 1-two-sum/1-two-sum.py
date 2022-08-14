class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        Set = set()
        idx = dict()
        diff = 0
        res = []
        
        for i in range(len(nums)):
            Set.add(nums[i])
            
            
        for i in range(len(nums)):
            idx[nums[i]] = i
            
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in Set and (idx[diff] != i):
                res.append(i)
                res.append(idx[diff]) 
                break
        return res