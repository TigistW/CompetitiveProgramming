class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        row = len(matrix)
        col = len(matrix[0])
        direction = {(0,1),(1,0),(-1,0),(0,-1)}
        self.memo = [[0 for i in range(len(matrix[0]))] for j in range(len(matrix))]
        res = 0
        for i in range(row):
          for j in range(col):
            res = max(res, self.dfs(matrix, i, j, direction)) 
        return res
        
    def dfs(self, matrix, i, j, direction):
      if self.memo[i][j] != 0:
        return self.memo[i][j]
      
      for x, y in direction:
        new_row = i + x
        new_col = j + y
        
        if new_row >= 0 and new_row < len(matrix) and new_col >= 0 and new_col < len(matrix[0]) and matrix[i][j] > matrix[new_row][new_col]:
          self.memo[i][j] = max(self.memo[i][j], self.dfs(matrix, new_row, new_col, direction))
      self.memo[i][j] += 1
      
      return self.memo[i][j]
    
               
            
'''
basic dfs...memoized

'''            
        
        
        