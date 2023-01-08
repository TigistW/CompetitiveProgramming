class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        less = []
        equ = []
        more = []
        
        for i in range(len(nums)):
          if nums[i] < pivot:
            less.append(nums[i])
          elif nums[i] > pivot:
            more.append(nums[i])
          else:
            equ.append(nums[i])
        
        less.extend(equ)
        less.extend(more)
        
        return less
          