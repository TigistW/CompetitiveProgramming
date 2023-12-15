class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
       
        outgoing = set()
        
        for i, j in paths:
            outgoing.add(i)
            
        for i, j in paths:
            if j not in outgoing:
                return j
            
      