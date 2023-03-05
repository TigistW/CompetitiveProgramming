class Solution:
    def minJumps(self, arr: List[int]) -> int:
        def validIdx(idx):
            return idx < len(arr) and idx >= 0 and idx not in vi
        
        duplicate = defaultdict(list)
        for i in range(len(arr)):
            duplicate[arr[i]].append(i)
                
        visited = set()
        vi= set()
        q = deque([0])
        count = 0
        while q:
            length_q = len(q)
            for i in range(length_q):
                popped = q.popleft()
                vi.add(popped)
                if popped == len(arr)-1:
                    return count
                for i in [-1,1]:   
                    if validIdx(popped+i):
                        q.append(popped+i)
                        
                if arr[popped] in visited:
                    continue
                visited.add(arr[popped])
                
                for j in duplicate[arr[popped]]:
                    if validIdx(j):
                        q.append(j)      
            count += 1
        # return count
        
        