class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        def BS(arr, left,right,target):
          if right >= left:
            mid = (left + right) // 2
            if arr[mid] == target:
              return True
            elif arr[mid] > target:
              return BS(arr,left,mid - 1,target)
            else:
              return BS(arr,mid + 1,right,target)
              
          else:
            return -1
        
        count = 0
        for i in range(len(nums)):
          if BS(nums,0,i - 1, nums[i] - diff) != -1 and  BS(nums,i + 1, len(nums) - 1, nums[i] + diff) != -1:
            count += 1
        return count
          