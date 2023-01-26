class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj_dic = defaultdict(list)
        for flight in flights:
            if flight[0] not in adj_dic:
                adj_dic[flight[0]] = defaultdict()
            adj_dic[flight[0]][flight[1]]=flight[2]

        q = deque([[src, 0, 0]])
        visited =  dict()
        visited[src] = 0
        min_cost = float('inf')
        while q:
            city, cost, trip = q.popleft()
            if city==dst and trip<=k+1:
                min_cost = min(min_cost, cost)
            if trip<=k:
                for i in adj_dic[city]:
                    if i not in visited or (cost+adj_dic[city][i]<visited[i]):
                        q.append([i, cost+adj_dic[city][i], trip+1])
                        visited[i] = cost+adj_dic[city][i]
        if min_cost==float('inf'):
            return -1
        else:
            return min_cost