class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        output = []
        for i in range(len(grid[0])):
            col = i
            success = True
            for row in range(len(grid)):
                if grid[row][col] == -1 and (col == 0 or grid[row][col-1] == 1):
                    success = False
                    break
                elif grid[row][col] == 1 and (col == len(grid[0]) - 1 or grid[row][col+1] == -1):
                    success = False
                    break
                else:
                    col = col + grid[row][col]
            if success:
                output.append(col)
            else:
                output.append(-1)
                
        return output
