class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
      summ = 0
      hashMap = dict()
      hashMap[0] = 1
      count = 0
      for i in range(len(nums)):
        summ += nums[i]
        if summ - k in hashMap and hashMap[summ - k] > 0:
          # hashMap[summ - k] -= 1
          count += hashMap[summ - k]
          
        if summ in hashMap:
          hashMap[summ] += 1
        else:
          hashMap[summ] = 1
        
      return count
          
        
          
          
        
        
        