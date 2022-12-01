class Solution:
    def nearestExit(self, M: List[List[str]], entrance: List[int]) -> int:
        from math import inf
        from collections import deque

        m, n = len(M), len(M[0])
        q = deque([(tuple(entrance), 0)])
        d = ((0, 1), (0, -1), (1, 0), (-1, 0))
        visited = set([tuple(entrance)])
        ans = inf
        
        while q:
            cur, step = q.popleft()
            x, y = cur
            for dx, dy in d:
                nx, ny = x + dx, y + dy
                if not (0 <= nx < m and 0 <= ny < n) or (nx, ny) in visited or M[nx][ny] == "+":
                    continue
                if (0 in (nx, ny) or nx == m - 1 or ny == n - 1):
                    ans = min(ans, step + 1)
                else:
                    visited.add((nx, ny))
                    q += ((nx, ny), step + 1),
        return (ans, -1)[ans == inf]
