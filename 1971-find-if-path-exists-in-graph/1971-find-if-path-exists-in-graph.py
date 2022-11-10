
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        for i, j in edges:
          graph[i].append(j)
          graph[j].append(i)
          
        visited = set()
        def dfs(node):
          if node == destination:
            return True
          if node not in visited:
            visited.add(node)
            for child in graph[node]:
              if dfs(child):
                return True
          return False
        return dfs(source)
          
        
          

            
            
            
          
        
        