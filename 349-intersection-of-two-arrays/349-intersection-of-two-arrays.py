class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        sets = set(nums1)
        insx = []
        
        for i in nums2:
          if i in sets:
            insx.append(i)
            sets.remove(i)
            
        return insx