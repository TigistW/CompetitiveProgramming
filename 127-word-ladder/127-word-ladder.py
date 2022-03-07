class Solution:
    def ladderLength(self, bw: str, ew: str, wl: List[str]) -> int:
        ws = set(wl)
        queue = deque([bw])
        visited = set()
        count = 1
        while queue:

            l = len(queue)
            for i in range(l):
                p = queue.popleft()
                if p == ew:
                    return count
                if p in visited:
                    continue
                visited.add(p)
                for i in range(len(p)):
                    for j in range(26):
                        c = chr(97 + j)
                        word = p[0:i] + c + p[i+1:]

                        if word in visited:
                            continue
                        if word in ws:
                            queue.append(word)
                            ws.remove(word)
            count +=1
        
        return 0
                            
                        
                            
                    
                    
                
                
        
        
