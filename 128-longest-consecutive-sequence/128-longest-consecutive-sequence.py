class Solution:
    def longestConsecutive(self, nums):
        long_seq = 0
        li = set(nums)
        length = 0
        
        for num in nums:
            if num - 1 not in li:
                cur = num
                length = 1

                while cur + 1 in li:
                    cur += 1
                    length += 1

                long_seq= max(long_seq, length)

        return long_seq
            