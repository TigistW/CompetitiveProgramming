class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        def backtrack(last, path, node):
          if node == last:
            ans.append(path + [node])
            return 
          else:
            path.append(node)
            for neighbour in graph[node]:
              backtrack(last, path, neighbour)
            path.pop()   
        ans = []
        start = 0
        last = len(graph) - 1
        backtrack(last, [], start)
        return ans