class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # nums.sort()
        # N =len(nums)
        # for i in range(N):
        #      if nums[i]==nums[i+1]:
        #             return nums[i]
        
        left = 0
        right = len(nums)-1
        count = 0
        dup = 0
        while(left <= right):
            mid = left+ (right-left)//2
            
            for num in nums:
                if num <= mid:
                    count+=1

            if count > mid:
                right=mid-1
                dup = mid
            else:
                left=mid+1
  
            count=0
        return dup
                    
            
    
            
            
            
            
            
                
            
                