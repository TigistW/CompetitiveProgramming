class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
      for i in range(len(matrix)):
        for j in range(len(matrix[0])):
          if self.inBound(i - 1, j - 1, matrix):
            if matrix[i - 1][j - 1] != matrix[i][j]:
              return False
      return True    
    def inBound(self, i, j, matrix) -> bool:
      return i >= 0 and j >= 0 and i < len(matrix) and j < len(matrix[0])
    
    