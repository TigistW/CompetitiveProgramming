class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def count(k):
            i , ans = 0, 0
            vals = defaultdict(int)
            for j in range(len(nums)):
                vals[nums[j]] += 1
                while len(vals) > k:
                    vals[nums[i]] -= 1
                    if not vals[nums[i]]:
                        del vals[nums[i]]
                    i += 1
                ans += j - i + 1
            return ans

        return count(k) - count(k-1)