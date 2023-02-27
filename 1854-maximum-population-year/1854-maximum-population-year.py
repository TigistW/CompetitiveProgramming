class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        popn = [0] * 101
        for i in logs:
            for i in range(i[0], i[1]):
                popn[i - 1950] += 1

        maxx = popn.index(max(popn))
        return maxx + 1950