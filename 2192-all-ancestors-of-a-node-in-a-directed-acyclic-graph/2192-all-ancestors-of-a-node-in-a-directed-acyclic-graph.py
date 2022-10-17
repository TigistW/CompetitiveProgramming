class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
      
      incoming = [0] * n
      graph = defaultdict(list)
      ans = [set() for i in range(n)]
      for i, j in edges:
        incoming[j] += 1
        graph[i].append(j)
        ans[j].add(i)
      queue = deque()
      
      for idx, j in enumerate(incoming):
        if j == 0:
          queue.append(idx)

      while queue:
        cur = queue.popleft()
        for vertice in graph[cur]:
          incoming[vertice] -= 1
          ans[vertice].update(ans[cur])
          if incoming[vertice] == 0:
            queue.append(vertice)
      return [sorted(i) for i in ans]   