class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        
        for i, j in edges:
          graph[i].append(j)
          graph[j].append(i)
          
        stack = []
        stack.append(source)
        visited = set()
        
        while stack:
          cur = stack.pop()
          if cur == destination:
            return True
          # print("cur", cur)
          if cur not in visited:
            for child in graph[cur]:
              stack.append(child)
          visited.add(cur)
        return False
            
            
            
          
        
        