
class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        
        if source == target: 
            return 0
        queue = deque()
        graph = defaultdict(set)
        
        routes = list(map(set, routes))
        seen, targets = set(), set()
        
        for i in range(len(routes)):
            if source in routes[i]:
                seen.add(i)
                queue.append((i, 1))
                
            if target in routes[i]: 
                targets.add(i)
                
            for j in range(i+1, len(routes)):
                if routes[j] & routes[i]:
                    graph[i].add(j)
                    graph[j].add(i)
        while queue:
            cur, cnt = queue.popleft()
            if cur in targets:
                return cnt
            for val in graph[cur]:
                if val not in seen:
                    queue.append((val, cnt + 1))
                    seen.add(val)
        return -1