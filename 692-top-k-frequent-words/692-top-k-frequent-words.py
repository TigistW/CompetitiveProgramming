class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:        
        
        ans=[]
        heap=[]
        count={}
        
        for word in words:
            count[word]=count.get(word,0)+1

        for key,v in count.items():
            heapq.heappush(heap,(-v,key))
            
        # print(heap)
        
        for i in range (k):
            ans.append(heapq.heappop(heap)[1])
        # print(count)
        
        return ans
