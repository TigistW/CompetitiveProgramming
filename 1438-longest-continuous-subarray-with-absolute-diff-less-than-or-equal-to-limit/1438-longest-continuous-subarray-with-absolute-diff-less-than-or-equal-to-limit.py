class Solution(object):
    def longestSubarray(self, nums, limit):
        minqueue = []
        maxqueue = []
        res = 0
        begin = 0
        for i, num in enumerate(nums):
            while minqueue and num < minqueue[-1]:
                minqueue.pop()
            minqueue.append(num)
            while maxqueue and num > maxqueue[-1]:
                maxqueue.pop()
            maxqueue.append(num)
            while maxqueue[0] - minqueue[0] > limit:
                if minqueue[0] == nums[begin]:
                    minqueue.pop(0)
                if maxqueue[0] == nums[begin]:
                    maxqueue.pop(0)
                begin += 1
            res = max(res, i - begin + 1)
        return res