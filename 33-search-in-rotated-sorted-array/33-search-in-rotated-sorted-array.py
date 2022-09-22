class Solution:
    def findPivot(self, nums):
        start, end, mid = 0, len(nums)-1, 1
        while start < end:
            mid = (start+end)//2
            if start==end-1 and nums[start]>nums[end]:
                return end
            if nums[mid]>nums[end]:
                start = mid
            elif nums[mid]<nums[start]:
                end = mid
            else:
                return len(nums)
        return mid

    def search(self, nums: List[int], target: int) -> int:
        pivot = self.findPivot(nums)
        if target>=nums[0]:
            start, end = 0, pivot-1
        else:
            start, end = pivot, len(nums)-1
        while start<=end:
            mid = (start+end)//2
            if nums[mid]<target:
                start = mid+1
            elif nums[mid]>target:
                end = mid-1
            else:
                return mid
        return -1                 