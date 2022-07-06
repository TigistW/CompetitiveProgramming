class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dic = dict()
        insx = []
        
        for i in nums1:
          if i not in dic:
            dic[i] = 1
          else:
            dic[i] += 1
        
        for i in nums2:
          if i in dic:
            if dic[i] > 0:
              insx.append(i)
              dic[i] -= 1
            
        return insx