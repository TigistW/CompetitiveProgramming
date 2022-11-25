class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n, MOD = len(arr), 1000000007
        left, right = [0] * n, [0] * n
        q = []
        for i, num in enumerate(arr + [0]):
            while q and num < arr[q[-1]]:
                idx = q.pop()
                left[idx] = idx - (q[-1] if q else -1)
            q.append(i)
        q = []
        for i, num in enumerate(reversed([0] + arr)):
            while q and num <= arr[q[-1]]:
                idx = q.pop()
                right[idx] = (q[-1] if q else n) - idx 
            q.append(n - i - 1)
        return sum(left[i] * arr[i] * right[i] for i in range(n)) % MOD