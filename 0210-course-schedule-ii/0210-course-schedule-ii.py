class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
      value = numCourses
      incoming = [0 for i in range(numCourses)]
      ans = []
      graph = collections.defaultdict(list)
      
      # if not prerequisites:
      #   return [i for i in range(numCourses)]
      for c,d in prerequisites:
        incoming[c] += 1
        graph[d].append(c)
        
      queue = deque()
      for i in range(numCourses):
        if incoming[i] == 0:
          queue.append(i)
          
      while queue:
        cur = queue.popleft()
        ans.append(cur)
        numCourses -= 1
        for dep in graph[cur]:
          incoming[dep] -= 1
          if incoming[dep] == 0:
            queue.append(dep)
      print(ans)
      if len(ans) == value:
        return ans
      return []
    
          
          
        
        
      
        
      
      
      