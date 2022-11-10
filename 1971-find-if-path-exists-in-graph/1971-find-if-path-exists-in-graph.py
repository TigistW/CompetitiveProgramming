class UnionFind:
  def __init__(self, n):
    self.parent = [i for i in range(n)]
    self.rank = [1 for i in range(n)]
    
  def find(self, node):
    while node != self.parent[node]:
      node = self.parent[node]
    return node
  def union(self, node_one, node_two):
    root_one = self.find(node_one)
    root_two = self.find(node_two)
    
    if root_one != root_two:
      if self.rank[root_one] < self.rank[root_two]:
        self.parent[root_one] = root_two
      elif self.rank[root_one] > self.rank[root_two]:
        self.parent[root_two] = root_one
      else:
        self.parent[root_one] = root_two
        self.rank[root_two] += 1
        
  def validPath(self, begin, end):
    return self.find(begin) == self.find(end)
    

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        uf = UnionFind(n)
        
        for i, j in edges:
          uf.union(i, j)
        return uf.validPath(source, destination)
          

            
            
            
          
        
        