class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()
        queue = deque()
        queue.append(0)
        
        while queue:
          cur = queue.popleft()
          for i in rooms[cur]:
            if i not in visited:
              queue.append(i)
          visited.add(cur)
        # print(visited)
        return len(visited) == len(rooms)
      
        