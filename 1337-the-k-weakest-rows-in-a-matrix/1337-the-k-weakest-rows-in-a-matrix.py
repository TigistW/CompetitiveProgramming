class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        heap = []
        
        for i in range(len(mat)):
          count = 0
          for val in mat[i]:
            if val == 1:
              count += 1
            
          heap.append((count,i))
          heapq.heapify(heap)
        
        weaks = []
        for i in range(k):
          val, index = heapq.heappop(heap)
          weaks.append(index)
          
        return weaks
          
          
            
      
            
            