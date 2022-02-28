class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:

        left = 1
        right = m*n
        small = 0
        count = 0
        minimum = min(m,n)
        while(left<=right):
            mid = left + (right -left) // 2  
            
            for i in range(1,m+1):
                j = mid // i
                count += min(j,n)

            # print(count," many less than or equal to", mid) 
            
            if count >= k:
                small = mid
                right = mid - 1
            else:
                left = mid + 1
            count = 0
        return small    
        
        
#         matrix=[]   
#         for i in range(1,m+1):
#             for j in range(1,n+1):
#                 matrix.append(i * j)  
    
#         heapq.heapify(matrix)
#         while k:
#             if len(matrix) != 0:
#                 cur=heapq.heappop(matrix)
#                 heapq.heapify(matrix)
#                 k=k-1
#             else:
#                 heap.heappop(matrix)
#         return cur


            

            