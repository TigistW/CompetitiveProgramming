class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        idx = 0
        dic = dict()
        
        for i in nums:
          if i not in dic:
            dic[i] = 1
          else:
            dic[i] += 1  
        
        for i in dic:
          if dic[i] > count:
            idx  = i
            count = dic[i]
        return idx
           
          
            
          
          