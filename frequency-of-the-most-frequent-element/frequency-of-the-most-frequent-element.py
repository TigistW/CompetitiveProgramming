class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        maxx=1
        prefix=[0]*(len(nums)+1)
        for i, num in enumerate(nums):
            prefix[i+1]=prefix[i]+num
        # print (nums,prefix,sep="\n")
        
        l,r=0,0
        while r<len(nums):
            summ=prefix[r+1]-prefix[l]
            tar=nums[r]*(r-l+1)
            
            if k>=(tar-summ):
                maxx=max(maxx,r-l+1)
                
                r+=1
                
            else:
                l+=1
                
        return maxx
                
            