# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        badnum=-1
        left=0
        right=n
        
        while(left<=right):
            mid=left+(right-left)//2
            if (isBadVersion(mid)==True):
                badnum=mid
                right=mid-1
            else:
                left=mid+1      
        return badnum
                
         