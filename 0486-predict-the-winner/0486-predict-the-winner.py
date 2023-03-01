class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        def recur(nums, i, j, turn):
            if i == j:
                return turn * nums[i]
                
            one = turn  * nums[i] + recur(nums, i + 1, j, -turn)
            two = turn  * nums[j] + recur(nums, i, j - 1, -turn)
            return turn * max(turn * one, turn * two)
                
        return recur(nums, 0,len(nums)-1,1) >= 0