class Solution:
    def isValid(self, pos):
      return 0 <= pos[0] < 8 and 0 <= pos[1] < 8
    
    def checkCell(self,king,dirs):
      i = 1
      new = (king[0] + (i * dirs[0]), king[1] + (i * dirs[1]))
      while self.isValid(new):
        new = (king[0] + (i * dirs[0]), king[1] + (i * dirs[1]))
        if self.isValid(new) and new in self.sets:
          return new
        i += 1
      return king
        
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
      self.queens = queens
      self.sets = set()
      for i, j in queens:
        self.sets.add((i, j))
        
      dirs = [(0,1), (1, 0), (-1, 0), (0, -1), (1,1), (-1,-1), (1, -1), (-1, 1)]
      queen = []
      for i in range(8):
        que = self.checkCell(king, dirs[i])
        if que != king:
          queen.append(que)
      return queen
        
        