class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]: 
        
        ans=[]
        heap=[]
        count={}

        for num in nums:
            count[num]=count.get(num,0)+1

        for key,v in count.items():
            heapq.heappush(heap,(-v,key))

        for i in range (k):
            ans.append(heapq.heappop(heap)[1])
        return ans

            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            