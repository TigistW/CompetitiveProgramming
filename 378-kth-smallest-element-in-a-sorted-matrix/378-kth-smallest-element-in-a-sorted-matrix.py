class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        while k:
            if len(matrix[0])!=0: 
                curr=heapq.heappop(matrix[0])
                heapq.heapify(matrix)
                k=k-1
            else:
                heapq.heappop(matrix)
            # print(matrix)
        return(curr)