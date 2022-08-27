class Solution:
    def maximumSum(self, nums: List[int]) -> int:
      
      dic = dict()
      
      for i in range(len(nums)):
        
        word = str(nums[i])
        word = list(word)
        summation = 0
        for k in word:
          summation += int(k)
          
        if summation not in dic:
          dic[summation] = []
          dic[summation].append(nums[i])
        else:
          dic[summation].append(nums[i])

      total = 0
      for val in dic:
        dic[val].sort()
        if len(dic[val]) >= 2:
          total = max(total,dic[val][-1] + dic[val][-2])

      if total == 0:
        return -1
        
      return total
          
        
          
          
          
          
        
        
        
        
        
      
      
          
      
          
          
        
          
        

