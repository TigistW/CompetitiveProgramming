class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int: 
        cost_list = [0] * len(cost)
        for i in range(len(cost)):
            if i - 1 >= 0:
                if i - 2 >=0:
                    cost_list[i] = cost[i] + min(cost_list[i-2], cost_list[i-1])
                else:
                    cost_list[i] = cost[i] + min(cost_list[i-1],0)  
            else:
                if i - 2 >=0:
                    cost_list[i] = cost[i] + min(0,cost_list[i-2])
                else:
                    cost_list[i] = cost[i]     
                    
        return min(cost_list[-1], cost_list[-2])