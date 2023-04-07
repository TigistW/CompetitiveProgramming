class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
       
        seen = set((row, col) for row in (0, m-1) for col in range(n) if grid[row][col]) | set(
            (row, col) for col in (0, n-1) for row in range(m) if grid[row][col])
        dq = deque(list(seen))
        while dq:
            i, j = dq.popleft()
            for p, q in [(i+1, j), (i-1,j), (i, j-1), (i, j+1)]:
                if 0 <= p < m and 0 <= q < n and grid[p][q] == 1 and (p, q) not in seen:
                    seen.add((p, q))
                    dq.append((p, q))
        total_land = sum(sum(row) for row in grid)
        return total_land - len(seen)