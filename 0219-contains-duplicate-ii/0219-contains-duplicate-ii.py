class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
      
      if k == 0:
        return False
      dic = defaultdict(int)
      for i in range(len(nums)):
        if nums[i] not in dic:
          dic[nums[i]] = i
        else:
          if math.fabs(dic[nums[i]] - i) <= k:
            return True
          dic[nums[i]] = i
          
      return False
          
          
      
      
     
      '''
      sliding window kinda 
      approach with a size upto k
      and keeping a dictionary of counts
      '''
      
      
      