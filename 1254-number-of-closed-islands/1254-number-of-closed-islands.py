class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
    
        def dfs(row, col):
            for nr, nc in ((row-1, col), (row, col+1), (row+1, col), (row, col-1)):
                if 0 <= nr < rows and 0 <= nc < cols and not grid[nr][nc]:
                    grid[nr][nc] = 2
                    dfs(nr, nc)
    
        rows, cols = len(grid), len(grid[0])
        for r in range(rows):
            if not grid[r][0]:
                grid[r][0] = 2
                dfs(r, 0)
            if not grid[r][cols - 1]:
                grid[r][cols - 1] = 2
                dfs(r, cols - 1)

        for c in range(cols):
            if not grid[0][c]:
                grid[0][c] = 2
                dfs(0, c)
            if not grid[rows - 1][c]:
                grid[rows - 1][c] = 2
                dfs(rows - 1, c)

        n = 0
        for r in range(1, rows):
            for c in range(1, cols):
                if not grid[r][c]:
                    dfs(r, c)
                    n += 1
    
        return n