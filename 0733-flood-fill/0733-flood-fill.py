class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
      def inBound(row, col):
        return 0 <= row < len(image) and 0 <= col < len(image[0]) and image[row][col] == start_color
      dxn = [(0,1), (1, 0), (-1, 0), (0, -1)] 
      stack = []
      start_color = image[sr][sc]
      stack.append((sr, sc))
      seen = set()
      while stack:
        row, col = stack.pop()
        if (row, col) not in seen:
          if image[row][col] == start_color:
            image[row][col] = newColor
            
            seen.add((row, col))
            for d in dxn:
              new_row = row + d[0]
              new_col = col + d[1]

              if inBound(new_row, new_col):
                stack.append((new_row, new_col))
      return image
            
            
      
        
      
    

            
        
            
    
        