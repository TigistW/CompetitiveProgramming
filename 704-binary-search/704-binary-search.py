class Solution:
    def search(self, nums: List[int], target: int) -> int:
      def BS(left,right):
        if left <= right:
          mid = (left + right) // 2 
          if nums[mid] == target:
            return mid
          elif nums[mid] < target:
            return BS(mid + 1, right)
          else:
            return BS(left,mid - 1)
           
        else:
          return -1
      
      
      return BS(0,len(nums) - 1)
            
        
        