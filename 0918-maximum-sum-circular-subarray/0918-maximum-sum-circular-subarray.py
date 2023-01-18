class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        pre = []
        for num in nums:
            pre.append(num if not pre else (pre[-1] + num))
        for num in nums:
            pre.append(num if not pre else (pre[-1] + num))

        l = len(nums)
        pq = []
        cnt = defaultdict(int)
        for i in range(l):
            heappush(pq, pre[i])
            cnt[pre[i]] += 1
        
        ans = max(nums)
        for rb in range(l - 1, 2 * l - 1):
            lb = rb - l + 1
            while pq and cnt[pq[0]] == 0:
                heappop(pq)
            ans = max(ans, pre[rb + 1] - pq[0])
            cnt[pre[lb]] -= 1
            cnt[pre[rb + 1]] += 1
            heappush(pq, pre[rb + 1])

        return ans
