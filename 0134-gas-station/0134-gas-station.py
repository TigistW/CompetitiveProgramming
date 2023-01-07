class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(cost) > sum(gas):
          return -1
        ans, index = 0, 0
        for i in range(len(cost)):
          ans += (gas[i] - cost[i])
          if ans < 0:
            ans = 0
            index = i + 1
        return index