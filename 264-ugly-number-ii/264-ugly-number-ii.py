class Solution:
    def nthUglyNumber(self, n: int) -> int:
        heap=[1]
        count=0
        curr=0
        prev=curr
        
        while count<n:
            
            prev=curr
            curr=heapq.heappop(heap)
            if prev!=curr:
                count+=1

                heapq.heappush(heap,2*curr)
                heapq.heappush(heap,3*curr)
                heapq.heappush(heap,5*curr)

            if count==n:
                return curr
            
            
        
        