class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
      self.parent = [i for i in range(len(edges) + 1)]
      self.size = [1 for i in range(len(edges) + 1)]
      ans = []
      for i, j in edges:
        if self.union(i, j):
          ans.append(self.union(i, j))
      return ans[-1]
      
    def find(self, node):
      while self.parent[node] != node: 
        node = self.parent[node]
      return self.parent[node]
  
    def union(self,node_one, node_two):
      res = []
      par_one = self.find(node_one)
      par_two = self.find(node_two)

      if par_one == par_two:
        res = [node_one, node_two]
        
      else:
        # if not same union the two based on their size
        if self.size[par_one] > self.size[par_two]:
          self.parent[par_two] = par_onw
          self.size[par_one] += self.size(par_two)
        elif self.size[par_one] < self.size[par_two]:
          self.parent[par_one] = par_two
          self.size[par_two] += self.size(par_one)
        else:
          self.parent[par_two] = par_one
          self.size[par_two] += 1
          
      return res
    

      