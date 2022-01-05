#https://leetcode.com/problems/reduce-array-size-to-the-half/

class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        diction = defaultdict(int)
        for i in arr:
            diction[i] += 1
        ano_arr = []
        for key in diction:
            ano_arr.append(diction[key])
        ano_arr.sort(reverse=True)
        count = 0
        total_len = 0
        for i in ano_arr:
            count += 1
            total_len += i
            if total_len >= len(arr)//2:
                break
        return count
