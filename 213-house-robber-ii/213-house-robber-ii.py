class Solution:
    def rob(self, nums: List[int]) -> int:
        def calculate (nums,one,two):
            for i in nums:
                max_money = max(one + i, two) 
                one = two 
                two = max_money
            return two
        
        one, two, max_money = 0, 0, 0
        
        if len(nums) != 1:
            val1 = calculate(nums[:-1],one,two)
            val2 = calculate(nums[1:],one,two)
            return max(val1,val2)
        else:
            return nums[0]
        