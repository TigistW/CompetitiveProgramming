class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for pair in adjacentPairs:
            graph[pair[0]].append(pair[1])
            graph[pair[1]].append(pair[0])
        start = None
        for i in graph:
            if len(graph[i]) == 1:
                start = i
                break
        queue = deque()
        queue.append(start)
        ans = []
        seen = set()
        while queue:
            cur = queue.popleft()
            for neighbour in graph[cur]:
                if neighbour not in seen:
                    queue.append(neighbour)
            seen.add(cur)
            ans.append(cur)
        return ans
                        
                
            
            