class Solution:
    def countPrimes(self, n: int) -> int:
      arr = [False for j in range(n)]
      count = 0
      for i in range(3, int(math.sqrt(n)) + 1, 2):
        if arr[i] == False:
          j = 0
          while i * (i + j) < n:
            arr[i * (i + j)] = True
            j += 1
            
      for i in range(3, n, 2):
        if arr[i] == False:
          count += 1
      if n <= 2:
        return count
      return count + 1
      
    
    
      
        
            
        
      
      
