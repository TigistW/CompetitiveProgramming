class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # for i in matrix:
        #     for j in i: 
        #         if j==target:
        #             return True
        # return False
        
        row=len(matrix)
        col=len(matrix[0])     
        left = 0
        right = (row * col) - 1
        
        while(left <= right):
            
            mid = left + (right - left) // 2

            count , midrow, midcol = 0 , 0 , 0
            for i in range(row): 
                for j in range (col):
                  count += 1
                  if count - 1 == mid:
                      midrow = i
                      midcol = j

            num = matrix[midrow][midcol]       
            
            # print("mid=",mid,"midcol=",midcol,"midrwo=",midrow,"num",num)
            
            if num==target:
                return True
            else:
                if target > num:
                    left = mid + 1 
                else:
                    right = mid - 1

                
                
                
                
            
            
        