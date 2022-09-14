class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        dic =dict()
        ans = [-1] * len(nums1)
        
        for i in range(len(nums1)):
          dic[nums1[i]] = i
          
        for i in range(len(nums2)):
          if nums2[i] not in dic:
            continue
            
          for j in range(i, len(nums2)):
            if nums2[j] > nums2[i]:
              ans[dic[nums2[i]]]=nums2[j]
              break
        return ans
              
            
          
          
          
          
              
            
            
            
              
              
              
              
            
            
            
        