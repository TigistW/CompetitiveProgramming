class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        
        wealth = 0
        summ = 0
        
        
        for i in accounts:
          for j in i:
            summ += j  
          wealth = max(wealth,summ)
          summ = 0
        return wealth
                    