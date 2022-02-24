class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        li = []
        li.append(self.bs(nums,target))
        li.append(self.bs(nums,target,False))
        
        return li
    def bs(self,nums,target,left=True):
        l = 0
        r = len(nums)-1
        best = -1
        while(l <= r):
            mid = l + (r-l) //2

            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r=  mid - 1

            else:
                best = mid
                if left:
                    r = mid-1
                else:
                    l = mid + 1 
        return best