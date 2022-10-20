class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        
        graph = defaultdict(list)
        incomingEdges = [0] * numCourses
        ancestory = [ set() for i in range(numCourses)]
        
        for i, j in prerequisites:
          graph[i].append(j)
          incomingEdges[j] += 1
          ancestory[j].add(i)
          
        queue = deque()
        for idx, j in enumerate(incomingEdges):
          if j == 0:
            queue.append(idx)

        while queue:
          cur = queue.popleft()
          for i in graph[cur]:
            incomingEdges[i] -= 1
            ancestory[i].update(ancestory[cur])
            if incomingEdges[i] == 0:
              queue.append(i)
          
        children = [set() for i in range(numCourses)]
        for idx, sets in enumerate(ancestory):
          for i in sets:
            children[i].add(idx)
            
        result = []
        for i, j in queries:
          if j in children[i]:
            result.append(True)
          else:
            result.append(False)
        return result  
      
'''
find the children of all the nodes and 
see if that query exists in that
combination of parent and child

'''


          
        
        