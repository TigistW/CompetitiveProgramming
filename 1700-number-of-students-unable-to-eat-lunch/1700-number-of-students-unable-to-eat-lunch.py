class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
      size = len(students)
      count = 0
      
      for i in range(size ** 2):
        # print("students",students,"sandwiches",sandwiches,"count",count)
        if len(students) != 0:
          cur = students.pop(0) 
          if cur == sandwiches[0]:
            sandwiches.pop(0)
            count += 1
          else:
            students.append(cur)
      return size - count
      
          
    