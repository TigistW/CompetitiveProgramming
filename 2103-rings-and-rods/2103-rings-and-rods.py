class Solution:
    def countPoints(self, rings: str) -> int:
        dic = defaultdict()
        count  = 0
        
        for i in range(0,len(rings),2):
          if rings[i + 1] not in dic: 
            dic[rings[i+1]] = []
            dic[rings[i+1]].append(rings[i])  
          else:
            dic[rings[i+1]].append(rings[i])
            
        for i in dic:
          sets =set(dic[i])
          if "B" in sets:
            if "G" in sets:
              if "R" in sets:
                count += 1      
        return count
          
            
            