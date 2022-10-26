class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        hashmap = {}
        
        for i in range(n):
            if i != n-1 and ((nums[i] == 0 and nums[i+1] == 0) or nums[i]%k ==0 and nums[i+1] % k == 0):
                return True
            if i != 0:
                nums[i] += nums[i-1]
                val = nums[i] % k
                if (val in hashmap and i - hashmap[val] > 1) or (val == 0):
                    return True
                hashmap[val] = i
            else:
                val = nums[i] % k
                hashmap[val] = i
        return False