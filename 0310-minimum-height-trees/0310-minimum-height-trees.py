class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        if n == 1:
          return [0]
        
        for i, j in edges:
          graph[i].append(j)
          graph[j].append(i)
          
        queue = []
        for i in graph:
           if len(graph[i]) == 1: 
              queue.append(i)
        centers = n
        while centers > 2:
          centers -= len(queue)
          new_queue = []
          while queue:
            cur_leaf = queue.pop(0)
            val = graph[cur_leaf].pop()
            graph[val].remove(cur_leaf) 
            graph.pop(cur_leaf)
            
            if len(graph[val]) == 1:
              new_queue.append(val)
          queue = new_queue
          # print(graph)
        return queue
                  