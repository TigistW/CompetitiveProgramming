class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        heap=[]
        for i in range(len(heights)-1):
            
            jump=heights[i+1]-heights[i]
            if jump>0:
                heapq.heappush(heap,jump)
            if len(heap)>ladders:
                num=heapq.heappop(heap)
                bricks-=num
            if bricks<0:
                return i
        return len(heights)-1
        
        
            
            
                    
                         
                
            