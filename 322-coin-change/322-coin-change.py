class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
#       bottom up
      dp = [inf] * (amount + 1)
      dp[0] = 0
    
      for i in range(1,amount + 1):
        for c in coins:
          if i - c >= 0:
            dp[i] = min(dp[i], dp[i - c] + 1)
            
      if dp[amount] == inf:
        return -1
      return dp[amount] 
            
        
      
      
      
      
      
      
      
#         count, vals, res = 0, 0,0
#         queue = deque()
#         queue.append(max(coins))
#         coins = coins[:-1]
        
#         while queue:
#             cur = queue.popleft()
#             if amount >= cur:
#                 vals = amount // cur
#                 count += vals 
#                 res += (vals * cur)
#                 amount -= (vals * cur)
                
#                 if len(coins) != 0:
#                     queue.append(max(coins)) 
#                     coins = coins[:-1]
#                 else:
#                     continue
#             else:
#                 if len(coins) != 0:
#                     queue.append(max(coins)) 
#                     coins = coins[:-1]
#                 else:
#                     return count
#         if amount == res:
#           return count
#         return -1 
            
            
        
            