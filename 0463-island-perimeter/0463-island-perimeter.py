class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m, n, peri = len(grid), len(grid[0]), 0
        for i in range(m):
            for j in range(n):
                peri += 4*grid[i][j]
                if i > 0:   peri -= grid[i][j]*grid[i-1][j]
                if i < m-1: peri -= grid[i][j]*grid[i+1][j]
                if j > 0:   peri -= grid[i][j]*grid[i][j-1]
                if j < n-1: peri -= grid[i][j]*grid[i][j+1]
                    
        return peri
        
        
        
        
        
          