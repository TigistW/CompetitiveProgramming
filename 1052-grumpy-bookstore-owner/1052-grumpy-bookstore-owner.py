class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        left, right, summ, max_cust = 0, 0, 0, 0
        while right < len(customers):
          while right - left != minutes:
            if grumpy[right] == 1:
              summ += customers[right]
            right += 1
          else:
            max_cust = max(max_cust, summ)
            if grumpy[left] == 1:
              summ -= customers[left]
            left += 1
        res = 0
        for i in range(len(customers)):
          if grumpy[i] == 0:
            res += customers[i]
        return res + max_cust
            
            
          