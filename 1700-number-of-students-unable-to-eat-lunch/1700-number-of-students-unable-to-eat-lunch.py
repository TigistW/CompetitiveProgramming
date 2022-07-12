class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
      std_size = len(students)
      count = 0
      
      while count < std_size:
        cur = students.pop(0)
        
        if cur == sandwiches[0]:
          sandwiches.pop(0)
          count = 0
        else:
          students.append(cur)
          count += 1
          
        if count == len(sandwiches):
          return count
        
      
          
    