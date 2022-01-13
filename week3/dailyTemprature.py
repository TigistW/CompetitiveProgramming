#https://leetcode.com/problems/daily-temperatures/
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ls = []
        siz = len(temperatures)
        result = [0]*siz
        for i in range(siz):
            while ls and ls[-1][0] < temperatures[i]:
                temp = ls.pop()
                result[temp[1]] = i - temp[1]
            ls.append((temperatures[i], i))
        return result
