class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n - 1:
            return -1

        adj = [list() for _ in range(n)]
        for connection in connections:
            adj[connection[0]].append(connection[1])
            adj[connection[1]].append(connection[0])

        numberOfConnectedComponents = 0
        visit = [False] * n
        for i in range(n):
            if not visit[i]:
                numberOfConnectedComponents += 1
                self.bfs(i, adj, visit)

        return numberOfConnectedComponents - 1

        
    def bfs(self, node, adj, visit):
        q = deque([node])
        visit[node] = True

        while q:
            node = q.popleft()
            for neighbor in adj[node]:
                if not visit[neighbor]:
                    visit[neighbor] = True
                    q.append(neighbor)