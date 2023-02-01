class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
      row, col = len(mat), len(mat[0])
      res = [[0 for j in range(col)] for i in range(row)]
      for i in range(row):
          for j in range(col):
              for rng in range(max(0, i-k), min(row, i+k+1)):
                  res[i][j]+=sum(mat[rng][max(0, j-k): min(col, j+k+1)])
      return res
