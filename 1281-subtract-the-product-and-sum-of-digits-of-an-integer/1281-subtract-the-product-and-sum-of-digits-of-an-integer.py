class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        summ = 0
        prd = 1
        
        n = str(n)
        for i in n:
          i = int(i)
          summ += i
          prd *= i
          
        return prd - summ