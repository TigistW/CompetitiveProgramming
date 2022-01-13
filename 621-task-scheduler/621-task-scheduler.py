class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        siz=len(tasks)
        if n==0:
            return siz
        
        dictt=defaultdict(int)
        for i in tasks:
            dictt[i]+=1
        dictt=dict(sorted(dictt.items(), key=lambda item:item[1], reverse=True))
        arr=list(dictt.values())
        output=(n+1)*arr[0]-n
        print(output)
        for i in range(1,len(arr)):
            if arr[i]==arr[0]:
                output+=1
            else:
                break
        if output<siz:
            return siz
        return output
      