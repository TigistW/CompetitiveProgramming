class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
      
        li = list(zip(plantTime, growTime))
        total_plant_time, earliest = 0, 0
        li.sort(key = lambda x: x[1],reverse = True)
        
        for i, j in li:
          total_plant_time += i
          earliest = max(earliest, total_plant_time + j)
        return earliest