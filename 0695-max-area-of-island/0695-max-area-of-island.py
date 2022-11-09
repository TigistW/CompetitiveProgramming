class UnionFind:
  def __init__(self, grid):
    n = len(grid)
    m = len(grid[0])
    
    self.parent = [[(i, j) for j in range(m)] for i in range(n)]
    self.rank = [[1 for i in range(m)] for j in range(n)]
    self.count = [[grid[j][i] for i in range(m)] for j in range(n)]
    self.maxArea = 0
    
  def find(self, vertice):
    while vertice != self.parent[vertice[0]][vertice[1]]:
      vertice = self.parent[vertice[0]][vertice[1]]
    return vertice
  
  def union(self, new_coord, cur_coord):
    root_one = self.find(new_coord)
    root_two = self.find(cur_coord)
    if root_one != root_two: 
      if self.rank[root_one[0]][root_one[1]] < self.rank[root_two[0]][root_two[1]]:  
        self.parent[root_one[0]][root_one[1]] = root_two
        self.count[root_two[0]][root_two[1]] += self.count[root_one[0]][root_one[1]]
        
      elif self.rank[root_one[0]][root_one[1]] > self.rank[root_two[0]][root_two[1]]:
        self.parent[root_two[0]][root_two[1]]= root_one
        self.count[root_one[0]][root_one[1]] += self.count[root_two[0]][root_two[1]]
      else:
        self.parent[root_one[0]][root_one[1]] = root_two
        self.count[root_two[0]][root_two[1]] += self.count[root_one[0]][root_one[1]]
        self.rank[root_two[0]][root_two[1]] += 1
        
  def maxAreaFound(self):
    print(self.count)
    for i in self.count:
      for j in i:
        self.maxArea = max(self.maxArea, j)
    
class Solution:
    def isValid(self,i, j, grid):
      return 0<= i< len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == 1
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
      dxn = [(1, 0), (0, 1), (-1, 0), (0, -1)]
      disjoint = UnionFind(grid)
      
      for i in range(len(grid)):
        for j in range(len(grid[0])):
          if grid[i][j] == 1:
            for row, col in dxn:
              new_i, new_j = i + row, j + col
              if self.isValid(new_i, new_j, grid):
                disjoint.union([new_i, new_j], [i, j])
      disjoint.maxAreaFound()
      return disjoint.maxArea
            
      
      
      
      
      
      
      
      
      
      
      
      
      
      
        