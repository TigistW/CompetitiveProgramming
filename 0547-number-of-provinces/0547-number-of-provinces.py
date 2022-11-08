class UnionFind:
  def __init__(self, n):
    self.parent = [i for i in range(n)]
    self.rank = [1 for i in range(n)]
    self.count = 0
    
  def find(self, vertice):
    while vertice != self.parent[vertice]:
      vertice = self.parent[vertice]
    return vertice
  
  def union(self, vert_one, vert_two):
    root_one = self.find(vert_one)
    root_two = self.find(vert_two)
    
    if root_one != root_two:
      if self.rank[root_one] > self.rank[root_two]:
        self.parent[root_two] = root_one
      elif self.rank[root_two] > self.rank[root_one]:
        self.parent[root_one] = root_two
      else:
        self.parent[root_one] = root_two
        self.rank[root_two] += 1
  def numOfProvinces(self):
    for i in range(len(self.parent)):
      if i == self.parent[i]:
        self.count += 1
    return self.count
  
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
      disjoint = UnionFind(len(isConnected))
      for i in range(len(isConnected)):
        for j in range(len(isConnected[0])):
          if isConnected[i][j] == 1:
            disjoint.union(i, j)
            
      disjoint.numOfProvinces()
      return disjoint.count
          
     