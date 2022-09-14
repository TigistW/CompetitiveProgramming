class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        stack = []
        
        ans = [-1]* len(nums)
        
        for i in range(len(nums) * 2):
          num_in_nums = nums[i % len(nums)]
          
          while stack and nums[stack[-1]] < num_in_nums:
              val = stack.pop()
              ans[val] = num_in_nums
          if i < len(nums):
            stack.append(i)
            
        return ans
          
          
            

        
  

