class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n=len(nums)
        diffFreq=[{} for x in range(n)]
        ans=0
        for i in range(1,n):
            for j in range(0,i):
                diff=nums[j]-nums[i]
                freqj=diffFreq[j].get(diff,0)
                ans+=freqj
                freqi=diffFreq[i].get(diff,0)
                diffFreq[i][diff]=freqi+1+freqj  
        return ans