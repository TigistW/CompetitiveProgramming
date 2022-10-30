class Solution:
    def isInBound(self, i, j, grid):
      return i >= 0 and j >= 0 and i < len(grid) and j < len(grid[0])
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        dist = 0
        queue = deque()
        queue.append((0,0,k,dist))
        dxn = [(0,1), (0,-1),(1, 0), (-1, 0)]
        visited = set()
        while queue:
          i, j, obs, dist = queue.popleft()
          if (i, j, obs) not in visited:
            if i == len(grid) - 1 and j == len(grid[0]) - 1 and obs >= 0:
              return dist 
            if obs >= 0:
              for l in dxn:
                new_i = i + l[0]
                new_j = j + l[1]
                if self.isInBound(new_i, new_j, grid):
                  if grid[new_i][new_j] == 1:
                    queue.append((new_i, new_j, obs - 1, dist + 1))
                  else:
                    queue.append((new_i, new_j, obs, dist + 1))
            visited.add((i, j, obs))
        return -1 
                            
              
            
            
            
            
          
          