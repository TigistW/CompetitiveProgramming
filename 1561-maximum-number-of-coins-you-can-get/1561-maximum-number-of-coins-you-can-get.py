class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        coins=0
        piles.sort()
        size = len(piles)
        piles = piles[size // 3:]
        
        for i in range(0,size - size // 3,2):
          coins += piles[i]
        return coins
      
      
      
      
      
      
#         coins=0
#         piles.sort()
        
#         while piles:
#           # print(piles)
#           piles = piles[1:-1]
#           coins += piles[-1]
#           piles = piles[:-1]
#         return coins
            
            