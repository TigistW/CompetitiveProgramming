class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        r = len(matrix)
        c = len(matrix[0])
        right = (r * c) - 1
        while left <= right:
          mid = (left + right) // 2
          col, row = mid % c, mid // c
          if matrix[row][col] == target:
            return True
          elif matrix[row][col] < target:
            left = mid + 1
          else:
            right = mid - 1
        return False
                 