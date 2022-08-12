class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        
        lis = [1,5,15]
        count = 0
        curr_hour = current.split(":")[0]
        curr_min = current.split(":")[1]
        
        true_hour = correct.split(":")[0]
        true_min = correct.split(":")[1]
        
        diff_hour = int(true_hour) - int(curr_hour)
        diff_min = int(true_min) - int(curr_min)

        if diff_min < 0:
          diff_hour -= 1
          diff_min += 60
          
        while diff_min != 0:
          
          if diff_min >= max(lis):
            val = diff_min // max(lis)
            count += val
            diff_min -= val * max(lis)
            
          else:
            lis = lis[:-1]
            
        return count + diff_hour
            
          
          
        
          
          
          