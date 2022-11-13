class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
      def inBound(row, col):
        return 0 <= row < len(image) and 0 <= col < len(image[0]) and image[row][col] == start_color and (row, col) not in seen
      dxn = [(0,1), (1, 0), (-1, 0), (0, -1)] 
      start_color = image[sr][sc]
      seen = set()
      def dfs(i, j):
        if image[i][j] == start_color:
          image[i][j] = newColor
        
        seen.add((i, j))
        for d in dxn:
          new_row = d[0] + i
          new_col = d[1] + j
          
          if inBound(new_row, new_col):
            dfs(new_row, new_col)
            
      dfs(sr, sc)
      return image
        
      
            
            
      
        
      
    

            
        
            
    
        