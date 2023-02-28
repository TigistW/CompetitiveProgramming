import collections
class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        count = collections.Counter(nums)
        maxx = []
        max_cnt = -1
        
        for i in count:
            if count[i] > max_cnt:
                max_cnt = count[i]
                
        for i in count:
            if count[i] == max_cnt:
                maxx.append(i)
                
        minn = math.inf
        for i in maxx:
            first = nums.index(i)
            second = len(nums) - nums[::-1].index(i)
            minn = min(minn, second - first)
        return minn

        
        