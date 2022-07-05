class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        num = []
        size = len(nums)
        for i in range(2 * size):
          # print(i, i % size)
          num.append(nums[i % size])  
        return num