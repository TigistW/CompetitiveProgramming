class Solution:
    
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        
#         start = image[sr][sc]
#         # print(start)
#         self.dfs(image,sr,sc,newColor,start)
#         return image
    
#     def dfs(self,image,sr,sc,newColor,start):
#         if sr < 0 or sc < 0 or sr > len(image) - 1 or sc > len(image[0]) - 1 or image[sr][sc] == newColor or image[sr][sc] != start:
            
#             return
#         image[sr][sc] = newColor
        
#         self.dfs(image,sr + 1,sc,newColor,start)
#         self.dfs(image,sr - 1,sc,newColor,start)
#         self.dfs(image,sr,sc + 1,newColor,start)
#         self.dfs(image,sr,sc - 1,newColor,start)

        def dfs (sr, sc):
            image[sr][sc] = newColor
            # print(start)
            for dix in direx:
                nr = sr + dix[0]
                nc = sc + dix[1]
                # print(nr,nc)
                if nr < 0 or nc < 0 or nr > len(image) - 1 or nc > len(image[0]) - 1 or image[nr][nc] != start: 
                    continue
                dfs(nr,nc)
            
        direx = [[0,1], [1,0], [-1,0],[0,-1]]
        start = image[sr][sc]
        if start != newColor:
            dfs(sr, sc)
        return image
        

            
        
            
    
        