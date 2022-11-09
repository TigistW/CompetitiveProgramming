class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        dic = Counter(nums)
        return [i for i in dic if dic[i] == 1]