class Solution(object):
    def maxPerformance(self, n, speed, efficiency, k):
        """
        :type n: int
        :type speed: List[int]
        :type efficiency: List[int]
        :type k: int
        :rtype: int
        """
        
        cur_sum, h = 0, []
        ans = -float('inf')
        
        for i, j in sorted(zip(efficiency, speed),reverse=True):
            while len(h) > k-1:
                cur_sum -= heappop(h)
            heappush(h, j)
            cur_sum += j
            ans = max(ans, cur_sum * i)
            
        return ans % (10**9+7)

        