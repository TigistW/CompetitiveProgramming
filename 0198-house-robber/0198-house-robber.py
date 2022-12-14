class Solution:
    def rob(self, nums: List[int]) -> int:
        one, two = 0, 0
        for i in nums:
            max_money = max(one + i, two)
            one = two
            two = max_money
            # print(one, two, max_money)
        return two      