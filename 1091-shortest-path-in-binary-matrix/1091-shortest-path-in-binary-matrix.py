class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        
        def isValid(cell):
            return 0 <= cell[0] < len(grid) and 0 <= cell[1] < len(grid[0])

        def bfs(start):
            dxn = ((0, 1), (1, 0), (1, 1), (-1, 0), (0, -1), (-1, 1), (1, -1), (-1, -1))
            queue = deque()
            queue.append(start)
            seen = set()
            ans = math.inf
            while queue:
                for q in range(len(queue)):
                    cur = queue.popleft()
                    
                    if cur[0] == len(grid) - 1 and cur[1] == len(grid) - 1:
                        ans =  min(cur[2], ans)
                    elif (cur[0], cur[1]) not in seen:
                        for v_i, v_j in dxn:
                            new_cell = (cur[0] + v_i, cur[1] + v_j, cur[2] + 1)
                            if isValid(new_cell) and grid[new_cell[0]][new_cell[1]] == 0:
                                queue.append(new_cell)
                        seen.add((cur[0], cur[1]))

            if ans == math.inf:
                return -1
            return ans
        if grid[0][0] == 1:
            return -1
        return bfs((0, 0, 1))
        