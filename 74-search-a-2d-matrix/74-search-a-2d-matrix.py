class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        right = len(matrix) - 1
        
        while left <= right:
          mid = (left + right) // 2
          print(left,mid,right)
          if target < matrix[mid][0]:
            # print("to the left")
            right = mid - 1
          elif target > matrix[mid][-1]:
            # print("to the right")
            left = mid + 1
          elif target >= matrix[mid][0] and target <= matrix[mid][-1]:
            # print("second search")
            begin = 0
            end = len(matrix[mid]) - 1
            
            while begin <= end:
              middle = (begin + end) // 2
              if matrix[mid][middle] == target:
                return True
              elif matrix[mid][middle] > target: 
                end = middle - 1
              else:
                begin = middle + 1
                
            return False
            
            
            