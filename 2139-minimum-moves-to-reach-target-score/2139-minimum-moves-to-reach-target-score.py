class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        count = 0
        
        if maxDoubles == 0:
          return target - 1
          
        while target > 1:
          
          if target % 2 == 0 and maxDoubles > 0:
            count += 1
            maxDoubles -= 1
            target /= 2
            
          elif maxDoubles == 0:
            count += target - 1
            break
            
          else:
            count += 1
            target -= 1
        # print(count) 
        return int(count)