class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
            
        def dfs(i, j, visited):
            if i not in graph or j not in graph:
                return -1.0
            if j in graph[i]:
                return graph[i][j]
            visited.add(i)
            for neighbor in graph[i]:
                if neighbor not in visited: 
                    temp = dfs(neighbor, j, visited)
                    if temp == -1.0:
                        continue 
                    return temp * graph[i][neighbor] 
            visited.remove(i)
            return -1.0 
        res = []
        graph = defaultdict(dict)
        for i in range(len(equations)):
            graph[equations[i][0]][equations[i][1]] = values[i]
            graph[equations[i][1]][equations[i][0]] = 1 / values[i]
            
        for i, j in queries:
            res.append(dfs(i, j, set()))
        return res 