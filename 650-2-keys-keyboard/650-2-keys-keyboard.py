class Solution:
    def minSteps(self, n: int) -> int:
        dp = [0 for i in range(n + 1)]
        dp[0] = 0
        dp[1] = 0
        
        def isprime(num):
          for n in range(2,int(num**0.5)+1):
              if num%n==0:
                  return False
          return True

        for i in range(2,n + 1):
          if isprime(i):
            dp[i] = i
          elif i % 2 == 0:
            dp[i] = dp[i // 2] + 2
          else:
            largest = 0
            for k in range(2, i):
              if i % k == 0:
                largest = k
            dp[i] = dp[largest] + dp[i // largest]
        return dp[-1]
            
            
            
            