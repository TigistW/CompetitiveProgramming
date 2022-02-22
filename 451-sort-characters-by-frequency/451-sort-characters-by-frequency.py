class Solution:
    def frequencySort(self, s: str) -> str:
        count={}
        heap=[]
        ans=""
        for i in s:
            if i in count:
                count[i]+=1
            else:
                count[i]=1
        
#         for i in s:
#             count[i]=count.get(s,0)+1
        print(count)
        for key,v in count.items():
            heapq.heappush(heap,(-v,key))
            
        print(heap)
        
        for i in range (len(heap)):
            value=heapq.heappop(heap)
            ans+=(-(value[0])*(value[1]))
        return str(ans)
    
        print(dic)