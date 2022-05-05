class Solution:
  def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
    def dfs(i: int, j: int) -> int:
      if i < 0 or i == len(grid) or j < 0 or j == len(grid[0]):
        return 0
      if grid[i][j] != 1:
        return 0

      grid[i][j] = 2

      return 1 + dfs(i + 1, j) + dfs(i - 1, j) + dfs(i, j + 1) + dfs(i, j - 1)

    return max(dfs(i, j) for i in range(len(grid)) for j in range(len(grid[0])))

















# class Solution:
#     def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
#         n = len(grid)
#         uf = UF(n)
#         print(uf.root)
#         for i in range(len(grid)):
#             for j in range(len(grid[i])):
#                 if grid[i][j] == 1:
#                     uf.union(i,j)
#         return uf.count
    
# class UF:
#     def __init__(self,size):
#         self.root = [i for i in range(size)]
#         self.count = size
    
#     def find(self,node): 
#         if self.root[node] != node:  
#             return self.find(self.root[node])
#         return self.root[node]
    
#     def union(self,node1,node2): 
#         node1_pare = self.find(node1)
#         node2_pare = self.find(node2)
#         if node1_pare != node2_pare:
#             self.root[node2_pare] = node1_pare
#             self.count -= 1

#     def count(self):
#         return self.count 