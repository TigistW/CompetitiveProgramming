class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        dic =dict()
        ans = [-1] * len(nums1)
        stack = []
        
        for j in range(len(nums1)):
          dic[nums1[j]] = j  
          
        for i in range(len(nums2)):
          if len(stack) == 0 and nums2[i] in dic:
            stack.append(nums2[i])
          elif stack and stack[-1]  >= nums2[i]: 
             stack.append(nums2[i])
          else:
            while stack and stack[-1] < nums2[i]:
              val = stack.pop()
              ans[dic[val]] = nums2[i]    
            if nums2[i] in dic:
              stack.append(nums2[i]) 
        return ans
              
                
                
                
              
              
            
            
          
            
              
            
          
          
          
          
              
            
            
            
              
              
              
              
            
            
            
        