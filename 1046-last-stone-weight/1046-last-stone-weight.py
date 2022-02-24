class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        N=len(stones)
        for i in range(N):
            stones[i]=stones[i]*-1
        stones.sort()
        heapq.heapify(stones)

            
        
        while len(stones)>=0:
            if len(stones)==0:
                return 0
            if len(stones)==1:
                return stones[0] * -1
            
            cur= heapq.heappop(stones)
            if cur == stones[0] and stones[0]:      
                cur=0 
                heapq.heappop(stones)
            else: 
                stones[0]=cur - stones[0]
                heapq.heapify(stones)
                
