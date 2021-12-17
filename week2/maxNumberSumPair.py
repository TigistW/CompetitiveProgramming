
#https://leetcode.com/problems/max-number-of-k-sum-pairs/

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        count = 0
        pairs = defaultdict(int)
        for num in nums:
            if pairs[k-num]:
                pairs[k-num] -= 1
                count += 1
                
            else:
                pairs[num] += 1
            
                
        return count