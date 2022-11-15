class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
      def dfs(i, stones, visited):
        visited.add(i)
        for j in range(len(stones)):
            if (stones[i][0] == stones[j][0] or stones[i][1] == stones[j][1]) and j not in visited:
                dfs(j, stones, visited)
                
      visited = set()
      count = 0
      for i in range(len(stones)):
          if i not in visited:
              dfs(i, stones, visited)
              count += 1

      return len(stones) - count